
def solve():
    s = input().strip('\n')
    _, year = s.split("'")
    k = len(year)
    year = int(year)
    cover = 0
    base10 = 10
    for _ in range(k - 1):
        cover += base10
        base10 *= 10

    while year < 1989 + cover:
        year += base10
    print(year)


n = int(input())
for _ in range(n):
    solve()
