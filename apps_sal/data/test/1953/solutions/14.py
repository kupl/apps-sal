from collections import Counter
n = int(input())
a = [int(s) for s in input().split()]
c = set(a)
d = Counter(a)
res = 0
summ = 0
for i in sorted(list(c)):
    for j in range(d[i]):
        if summ <= i:
            res += 1
            summ += i
        else:
            break
print(res)
