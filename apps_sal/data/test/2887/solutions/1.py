# cook your dish here
n = int(input())
v = [int(x) for x in input().split()]
t = [int(x) for x in input().split()]
a = []
for i in range(n):
    a.append(v[i])
    c = 0
    for j in range(len(a)):
        k = a[j] - t[i]
        if k >= 0:
            c += t[i]
            a[j] = k
        else:
            c += a[j]
            a[j] = 0
    print(c, end=" ")
