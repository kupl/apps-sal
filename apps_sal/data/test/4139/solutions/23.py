def f(n):
    if n == 1:
        yield "7"
        yield "5"
        yield "3"
    else:
        for i in f(n - 1):
            yield i + "7"
            yield i + "5"
            yield i + "3"


n = int(input())
ans = 0
for j in range(1, 10):
    for i in f(j):
        if len(set(i)) == 3 and int(i) <= n:
            ans += 1
print(ans)
