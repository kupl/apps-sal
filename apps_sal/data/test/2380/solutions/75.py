import sys
n, m = list(map(int, input().split()))
a = sorted(list(map(int, input().split())))
b = []

for _ in range(m):
    b += [list(map(int, input().split()))]
b = sorted(b, key=lambda x: x[1], reverse=True)

for i in range(m):
    for j in range(b[i][0]):
        if a[0] < b[i][1]:
            a.pop(0)
            a.append(b[i][1])
        else:
            print((sum(a)))
            return
print((sum(a)))
            


