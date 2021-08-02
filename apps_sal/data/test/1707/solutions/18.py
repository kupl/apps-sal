n = int(input())
ls = list(map(int, input().split()))
ls = [abs(i) for i in ls]
ls.sort()
i = 0
j = 1
res = []
try:
    while True:
        while ls[j] <= 2 * ls[i]: j += 1
        res.append(j - i - 1)
        i += 1
except:
    while i != n:
        res.append(j - i - 1)
        i += 1
print(sum(res))
