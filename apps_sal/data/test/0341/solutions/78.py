"""
Created on Tue Sep  8 22:36:36 2020

@author: liang
"""
(N, K) = list(map(int, input().split()))
(R, S, P) = list(map(int, input().split()))
T = input()
hand = {'r': P, 's': R, 'p': S}
ans = 0
for i in range(K):
    s = str()
    tmp = i
    while tmp < N:
        s += T[tmp]
        tmp += K
    count = 1
    prev = str()
    for j in range(len(s)):
        if s[j] == prev:
            count += 1
        else:
            count = 1
        if count % 2 == 0:
            continue
        prev = s[j]
        '\n        if s[j] == "r":\n            ans += P\n        elif s[j] == "s":\n            ans += R\n        else:\n            ans += S\n        '
        ans += hand[s[j]]
print(ans)
