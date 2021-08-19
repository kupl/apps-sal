class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        from collections import defaultdict
        self.ans = 1

        def get(s, l, n):
            # print(l,n,len(s))
            if n == len(s):
                dic = defaultdict(int)
                for i in l:
                    dic[i] += 1
                z = True
                for i in dic:
                    if dic[i] > 1:
                        z = False
                        break
                if z:
                    self.ans = max(self.ans, len(l))
                return
            i = n
            cur = ''
            # print(\"here\")
            for j in range(i, len(s)):
                # print(j)
                cur += s[j]
                # print(cur)
                get(s, l + [cur], j + 1)

        get(s, [], 0)
        return self.ans

        # dic=defaultdict(int)
        # n=len(s)
        # i=0
        # ans=[]
        # while i<n:
        #     cur=''
        #     j=i
        #     z=True
        #     while j<n:
        #         cur+=s[j]
        #         if dic[cur]==0:
        #             ans.append(cur)
        #             z=False
        #             dic[cur]=1
        #             j+=1
        #             break
        #         else:
        #             j+=1
        #     i=j
        #     if z:
        #         ans[-1]=ans[-1]+cur
        # return len(ans)
