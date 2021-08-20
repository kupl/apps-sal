import sys
S = input()
K = int(input())
for i in range(K):
    if S[i] != '1':
        ans = S[i]
        break
else:
    ans = '1'
print(ans)
