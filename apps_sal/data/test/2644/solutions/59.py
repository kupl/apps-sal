N = int(input())
P = list(map(int, input().split()))

bef = 1
ans = []
for i in range(N):
    if P[i] == bef:
        for j in range(i, bef - 1, -1):
            P[j], P[j - 1] = P[j - 1], P[j]
            ans.append(j)
        bef = i + 1

if len(ans) != (N - 1) or P != sorted(P):
    print('-1')
else:
    print('\n'.join(map(str, ans)))
