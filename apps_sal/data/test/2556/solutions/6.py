n = int(input())
for i in range(n):
    c, s = map(int, input().split())
    r = s // c
    # s%c部屋r+1
    l = s % c
    ans = r * r * (c - l) + (r + 1)**2 * l
    print(ans)
