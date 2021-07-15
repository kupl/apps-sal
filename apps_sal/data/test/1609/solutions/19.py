n = int(input())
inp = list(map(int,input().split(' ')))
used = set(inp)
seen = set()
toadd = set(i+1 for i in range(n) if i+1 not in used)
res = []
for num in inp:
    if num < 1 or num > n or num in seen:
        num = toadd.pop()
    else:
        seen.add(num)
    res.append(num)
print(*res)
