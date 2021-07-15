n = int(input())
inp = list(map(int,input().split(' ')))
used = set(inp)
seen = set()
toadd = {i+1 for i in range(n)}.difference(used)
res = []
for num in inp:
    if num < 1 or num > n or num in seen:
        num = toadd.pop()
    else:
        seen.add(num)
    res.append(num)
print(*res)
