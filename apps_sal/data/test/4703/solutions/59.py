S = list(input())
N = len(S) - 1
ans = 0
for i in range(1 << N):
    a = S[0]
    for j in range(N):
        if(i >> j) & 1 == 0:
            a += S[j + 1]
        else:
            x = int(a)
            ans += x
            a = S[j + 1]
    x = int(a)
    ans += x
print(ans)
