import sys
n = int(input())

ans = []

if n == 1:
    print('1')
    return

for i in range(n // 2):
    for j in range(n // 2):
        if i**j <= n:
            ans.append(i**j)

print(max(ans))
