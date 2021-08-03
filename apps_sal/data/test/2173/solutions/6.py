import operator

n = int(input())

a = list((v, k) for k, v in enumerate(map(int, input().split())))
a.sort(key=operator.itemgetter(0))
# print(a)

cur = 0
b = [0] * n

for i in range(n):
    x = a[i][0]
    if x > cur:
        cur = x + 1
        b[a[i][1]] = str(x)
    else:
        b[a[i][1]] = str(cur)
        cur += 1

#b = sorted(b,key=itemgetter(1))

print(' '.join(b))
