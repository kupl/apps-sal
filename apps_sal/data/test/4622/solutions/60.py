import sys
n = int(input())
lst = list(map(int, input().split()))

lst.sort()
for i in range(n - 1):
    if lst[i] == lst[i + 1]:
        print('NO')
        return
print('YES')
