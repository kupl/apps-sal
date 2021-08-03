N, M = map(int, input().split())

l = 0
r = N

for i in range(M):
    L, R = map(int, input().split())

    if L > l:
        l = L

    if R < r:
        r = R

    ans = r - l + 1
    if ans < 0:
        print(0)
        break

else:
    print(ans)
