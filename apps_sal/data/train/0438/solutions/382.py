class UnionFind:
    
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0]*n
        self.size = [0]*n
        self.groupCount = [0]*(n+1)
    
    def find(self, x):
        if x != self.parent[x]:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def add(self, x):
        self.size[x] = 1
        self.groupCount[1] += 1
    
    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return False
        self.groupCount[self.size[px]] -= 1
        self.groupCount[self.size[py]] -= 1
        if self.rank[px] > self.rank[py]:
            self.parent[py] = px
            self.size[px] += self.size[py]
            self.size[py] = 0
        elif self.rank[py] > self.rank[px]:
            self.parent[px] = py
            self.size[py] += self.size[px]
            self.size[px] = 0
        else:
            self.parent[px] = py
            self.size[py] += self.size[px]
            self.size[px] = 0
            self.rank[py] += 1
        self.groupCount[self.size[px]] += 1
        self.groupCount[self.size[py]] += 1
        return True
    
    def getSize(self, i):
        px = self.find(i)
        return self.size[px]
    
class Solution:
    
    def findLatestStep(self, arr: List[int], m: int) -> int:
        disjoint = UnionFind(len(arr))
        ans = - 1
        val = [0]*len(arr)
        for k in range(len(arr)):
            index = arr[k] - 1
            val[index] += 1
            disjoint.add(index)
            if index > 0 and val[index] == val[index-1]:
                disjoint.union(index, index - 1)
            if index + 1 < len(val) and val[index] == val[index+1]:
                disjoint.union(index, index + 1)
            #print(k, disjoint.groupCount)
            if disjoint.groupCount[m] > 0:
                ans = k + 1
            '''
            i = 0
            while i < len(arr):
                if val[i] == 1 and disjoint.getSize(i) == m:
                    i += disjoint.getSize(i)
                    ans = k + 1
                    continue
                i += 1
            '''
            #print(k, disjoint.size, val)
        return ans 
    
    '''
    def findLatestStep(self, arr: List[int], m: int) -> int:
        def check(i):
            val = [0]*len(arr)
            for k in range(i+1):
                val[arr[k]-1] = 1
            count = 0
            success = False
            for k in range(len(val)):
                if val[k] > 0:
                    count += 1
                else:
                    if count == m:
                        success = True
                        break
                    count = 0
            if count == m:
                success = True
            return success                
            
        left = 0
        right = len(arr)
        while left < right:
            mid = left + (right - left) //2
            if not check(mid):
                right = mid
            else:
                left = mid + 1
        print(left)
        if left == 0 and not check(left):
            return -1
        else:
            return left
    '''

