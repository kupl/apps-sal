n = int(input())
L = list(map(int, input().split()))
f = False
for i in range(n):
    j = L[i]
    k = L[j - 1]
    m = L[k - 1]
    if i == m - 1:
        f = True
        break
print('YES' if f else 'NO')
