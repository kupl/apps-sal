n, m = map(int, input().split())
tasks = list(map(int, input().split()))

bank = [0]*n
zeros = n
res = []
for t in tasks:
    if bank[t-1] == 0:
        zeros -= 1
    bank[t-1] += 1
    if zeros == 0:
        for i in range(n):
            bank[i] -=1
            if bank[i] == 0:
                zeros += 1
        res.append(1)
    else:
        res.append(0)

print(*res, sep='')
