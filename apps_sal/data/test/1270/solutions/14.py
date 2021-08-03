n = int(input())
res = list()
while n >= 2:
    res.append(2)
    n -= 2
if n == 1:
    res[0] += 1
print(len(res))
print(' '.join(map(str, res)))
