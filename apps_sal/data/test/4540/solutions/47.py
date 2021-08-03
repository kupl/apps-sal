n = int(input())
As = list(map(int, input().split()))
S = 0
for i in range(n - 1):
    S += abs(As[i] - As[i + 1])
S += abs(As[0]) + abs(As[n - 1])
for i in range(n):
    if i == 0:
        sb1 = abs(As[i])
        sb2 = abs(As[i] - As[i + 1])
        ad = abs(As[i + 1])
    elif i == n - 1:
        sb1 = abs(As[i - 1] - As[i])
        sb2 = abs(As[i])
        ad = abs(As[i - 1])
    else:
        sb1 = abs(As[i - 1] - As[i])
        sb2 = abs(As[i] - As[i + 1])
        ad = abs(As[i - 1] - As[i + 1])

    ans = S - sb1 - sb2 + ad
    print(ans)
