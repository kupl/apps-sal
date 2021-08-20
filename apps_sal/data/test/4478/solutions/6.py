k = int(input())
n = int(input())
a = list(map(int, input().split()))
d = {}
suma = sum(a)
for i in range(n):
    d[suma - a[i]] = [1, i + 1]
ans = False
for i in range(k - 1):
    n = int(input())
    a = list(map(int, input().split()))
    suma = sum(a)
    for j in range(n):
        if suma - a[j] in d and (not d[suma - a[j]][0] == i + 2):
            print('YES')
            print(i + 2, j + 1)
            print(d[suma - a[j]][0], d[suma - a[j]][1])
            ans = True
            break
        else:
            d[suma - a[j]] = [i + 2, j + 1]
    if ans:
        break
if not ans:
    print('NO')
