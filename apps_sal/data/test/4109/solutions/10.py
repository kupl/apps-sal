from itertools import product

n,m,x = list(map(int, input().split()))
book = []
for i in range(n):
    book.append(list(map(int, input().split())))

ans = 10 ** 5 * n
flag = False
for i in product([0,1], repeat=n):
    price = 0
    skill = [0] * m
    for index_, bit in enumerate(i):
        if bit:
            for j in range(m):
                skill[j] += book[index_][ j + 1]
            price += book[index_][0]
    if all(v >= x for v in skill):
        ans = min(ans, price)
        flag = True
if flag:
    print(ans)
else:
    print(-1)
