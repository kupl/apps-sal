class Solution:
    def canReorderDoubled(self, A: List[int]) -> bool:
        cache=Counter(A)
        c_list=sorted(list(cache),key=abs)
        for x in c_list:
            if cache[x]>cache[2*x]:
                return False
            cache[2*x]-=cache[x]
        return True
        
        '''
        if not A:
            return True
        positive_heap = []
        negative_heap = []
        zero = 0
        positive_d = defaultdict(int)
        negative_d = defaultdict(int)
        for i in A:
            if i == 0:
                zero += 1
            elif i < 0:
                heappush(negative_heap, -i)
                negative_d[-i] += 1
            else:
                heappush(positive_heap, i)
                positive_d[i] += 1
        if zero % 2 != 0:
            return False
        if not self.check(positive_heap, positive_d):
            return False
        if not self.check(negative_heap, negative_d):
            return False
        return True
    
    def check(self, h, d):
        for _ in range(len(h)):
            i = heappop(h)
            if d[i] == 0:
                continue
            if 2*i not in d:
                return False
            elif d[2*i] < d[i]:
                return False
            else:
                d[2*i] -= d[i]
                d[i] = 0
        return True
    '''

