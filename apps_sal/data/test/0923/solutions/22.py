n = int(input())

z = [int(x) for x in input().split()]
w = []

for i in range(n):
    if i % 2 == 0:
        if z[i] <= i:
            w.append(i - z[i])
        else:
            w.append(n - z[i] + i)
    else:
        if i <= z[i]:
            w.append(z[i] - i)
        else:
            w.append(z[i] + n - i)

for i in range(n - 1):
    if w[i] != w[i+1]:
        print('No')
        return

print('Yes')

