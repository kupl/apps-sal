n = int(input())
inp = list(map(int, input().split(' ')))
used = set(x for x in inp if x > 0 and x <= n)
toadd = {i + 1 for i in range(n)}.difference(used)
res = []
for num in inp:
    if num in used:
        used.remove(num)
    else:
        num = toadd.pop()
    res.append(num)
print(*res)
