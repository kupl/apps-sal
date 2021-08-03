tmp = [int(i) for i in input().split()]
n = tmp[0]
d = tmp[1]

a = [int(i) for i in input().split()]
a.sort()
m = int(input())

out = 0

for i in range(0, m):
    if i < len(a):
        out = out + a[i]
    else:
        out = out - d

print(out)
