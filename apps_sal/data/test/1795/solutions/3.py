n = int(input())
a = list(map(int, input().split()))
a = list(map(lambda x: x - 1, a))
f = False
for i in a:
    if a[a[a[i]]] == i:
        f = True
        break
print('YES' if f else 'NO')
