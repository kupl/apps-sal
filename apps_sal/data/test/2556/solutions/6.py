n = int(input())
for i in range(n):
    (c, s) = map(int, input().split())
    r = s // c
    l = s % c
    ans = r * r * (c - l) + (r + 1) ** 2 * l
    print(ans)
