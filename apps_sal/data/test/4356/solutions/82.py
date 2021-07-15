import sys
n, m = list(map(int, input().split()))
a, b = [], []

for _ in range(n):
    a.append(input())
for _ in range(m):
    b.append(input())

for i in range(0, n-m+1):
    for j in range(0, n-m+1):
        for k in range(m*m):
            if a[i+k//m][j+k%m] != b[k//m][k%m]:
                break
            elif k == m*m-1:
                print('Yes')
                return
print('No')

