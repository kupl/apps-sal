
n = int(input())

f = list([int(x) - 1 for x in input().split()])

for i in range(len(f)):
    if f[f[f[i]]] == i and f[f[i]] != i:
        print('YES')
        return

print('NO')

