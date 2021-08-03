class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        #         dic = {}
        #         def count_cluster(y,x,cur_count):
        #             length = 0
        #             if y[x-1] == 0:
        #                 if x <n:
        #                     if y[x+1] ==0:
        #                         # ...0x0...
        #                         y[x] = 1
        #                         dic[x] = x
        #                         if m==1:
        #                             cur_count+=1
        #                     else:
        #                         # ...0x#...
        #                         oldr = y[x+1]
        #                         y[x] = 1 + y[x+1]
        #                         y[dic[x+1]] = y[x]
        #                         dic[x] = dic[x+1]
        #                         dic[dic[x+1]] = x
        #                         if oldr == m-1:
        #                             cur_count +=1
        #                         if oldr == m:
        #                             cur_count -=1
        #                 else:
        #                     # ...0x
        #                     y[x] = 1
        #                     dic[x] = x
        #                     if m==1:
        #                         cur_count+=1
        #             else:
        #                 if x <n:
        #                     if y[x+1] ==0:
        #                         # ...#x0...
        #                         oldl = y[x-1]
        #                         y[x] = y[x-1] +1
        #                         y[dic[x-1]] = y[x]
        #                         dic[x] = dic[x-1]
        #                         dic[dic[x-1]] = x
        #                         if oldl == m-1:
        #                             cur_count +=1
        #                         if oldl == m:
        #                             cur_count -=1
        #                     else:
        #                         # ...#x#...
        #                         oldr = y[x+1]
        #                         oldl = y[x-1]
        #                         y[x] = y[x-1] + 1 + y[x+1]
        #                         temp = dic[x-1]

        #                         y[dic[x-1]] = y[x]
        #                         dic[dic[x-1]] = dic[x+1]

        #                         y[dic[x+1]] = y[x]
        #                         dic[dic[x+1]] = temp

        #                         if oldr==m:
        #                             cur_count -= 1
        #                         if oldl ==m:
        #                             cur_count-=1
        #                         if oldr+oldl == m-1:
        #                             cur_count+=1
        #                 else:
        #                     # ...#x
        #                     oldl = y[x-1]
        #                     y[x] = y[x-1] +1
        #                     y[dic[x-1]] = y[x]
        #                     dic[x] = dic[x-1]
        #                     dic[dic[x-1]] = x
        #                     if oldl == m-1:
        #                         cur_count +=1
        #                     if oldl == m:
        #                         cur_count -=1

        #             return cur_count
        #         n = len(arr)
        #         s = [0] * (n+1)
        #         last = -1
        #         cur_count = 0
        #         for idx,x in enumerate(arr):
        #             cur_count=count_cluster(s,x,cur_count)
        #             if cur_count>0:
        #                 last = idx+1
        #         return last

        # gonna try the union-find method
        def find(parent, x):
            if x == parent[x]:
                return x
            parent[x] = find(parent, parent[x])
            return parent[x]
        n = len(arr)
        parent = [0 for x in range(n + 1)]
        size = [0] * (n + 1)
        count = [0] * (n + 1)
        ans = -1
        for i, pos in enumerate(arr):

            size[pos] = 1
            count[1] += 1
            parent[pos] = pos
            for j in [-1, 1]:
                if (pos + j <= n) and (pos + j > 0) and (parent[pos + j] != 0):
                    x = find(parent, pos + j)
                    y = find(parent, pos)
                    if x != y:

                        count[size[x]] -= 1
                        count[size[y]] -= 1
                        parent[x] = y
                        size[y] += size[x]
                        count[size[y]] += 1
            if count[m] > 0:
                ans = i + 1
        return ans
