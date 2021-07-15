n, m, x = list(map(int, input().split()))
ans = 10 ** 9
books = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(2 ** (n + 1)):
    skill = [0 for _ in range(m)]
    money = 0

    for j in range(n):
        if i >> j & 1:
            book = books[j]
            money += book[0]
            for k, b in enumerate(book[1:]):
                skill[k] += b
    if all(s >= x for s in skill):
        ans = min(ans, money)
print((ans if ans != 10 ** 9 else - 1))

