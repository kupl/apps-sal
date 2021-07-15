N = int(input())
num = list(map(int, input().split()))

ans = 0
r = 0
sumz = 0
for l in range(N):
    if r < l: r = l

    while (r < N) and (num[r] + sumz) == (sumz ^ num[r]):
        sumz += num[r]
        r += 1

    ans += r-l
    sumz -= num[l]

print(ans)

