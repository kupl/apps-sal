
n = int(input())
a = [int(i) for i in input().split()]
a = [(a[i], i) for i in range(len(a))]
a.sort(reverse=True)

s = 0
order = []
for i in range(len(a)):
    s += a[i][0] * i + 1
    order.append(a[i][1])
print(s)
print(' '.join([str(i + 1) for i in order]))
