n, a, b = map(int, input().split())

res = 0
for i in range(1, n + 1):
    tmp = sum([int(elem) for elem in list(str(i))])
    if a <= tmp and tmp <= b:
        res += i
print(res)
