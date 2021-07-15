class Solution:
    def countTriplets(self, a: List[int]) -> int:
        p = [a[0]]
        for i in range(1,len(a)):
            p.append(p[-1]^a[i])
        # d=dict()
        ans = 0
        # print(p)
        for i in range(len(a)-1):
            for j in range(i+1,len(a)):
                v = p[j]^p[i]^a[i]
                for k in range(j,len(a)):
                    vv= p[k]^p[j]
                    if v==vv:
                        # print(i,j,k)
                        ans+=1
        #         v = p[j]^p[i]
        #         if v not in d:
        #             d[v] = list()
        #         d[v].append((i,j))
        # for i in d:
        #     d[i].sort()
        # print(d)
        # for i in d:
        #     for x in range(1,len(d[i])):
        #         if abs(d[i][x][0]-d[i][x-1][1])<=1:
        #             ans +=1
        return ans
