n, m = map(int, input().split())
f = [int(x) for x in input().split()]
b = [int(x) for x in input().split()]
list = [0] * 100001

for i in range(n):
    if list[f[i]] != 0:
        list[f[i]] = -1
    else:
        list[f[i]] = i + 1

for item in b:
    if list[item] == 0:
        print('Impossible')
        return

for item in b:
    if list[item] == -1:
        print('Ambiguity')
        return

output = [list[i] for i in b]

print('Possible')
print(' '.join([str(x) for x in output]))
