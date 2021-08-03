s, c = list(map(int, input().split()))

if (2 * s == c):
    ans = s

elif (2 * s > c):
    ans = c // 2

else:
    ans = s
    tar = c - 2 * s

    ans += tar // 4


print((int(ans)))
