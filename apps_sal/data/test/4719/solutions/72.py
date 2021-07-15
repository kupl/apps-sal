#75 C - 怪文書
import collections
n = int(input())
S = [input() for _ in range(n)]

cnt = collections.Counter(S[0])
for s in S[1:]:#O (50)
    for a in cnt.keys():# O(26)
        if a in s:# O(50)
            cnt[a] = min(cnt[a],s.count(a))# O(50)
        else:
            cnt[a] = 0
            
ans = [key*value for key,value in cnt.items() if value > 0]
ans = sorted(ans,reverse = False)
print(''.join(ans))
