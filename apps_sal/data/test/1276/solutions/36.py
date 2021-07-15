from collections import Counter
N = int(input())
S = input()
D = Counter(S)
ans = 1
for d in D.values():
    ans *= d

if len(D.values()) < 3:
    ans = 0

for i in range(N):
    for x in range(1, (N-i+1)//2):
        if S[i] != S[i+x] and S[i+x] != S[i+2*x] and S[i+2*x] != S[i]:
            ans -= 1
print(ans)
