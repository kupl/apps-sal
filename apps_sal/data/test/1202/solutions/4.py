n = int(input())
a = []
b = []
for i in range(n):
    x, y = map(int, input().split())
    a.append(x)
    b.append(y)
i = j = 0
ans1 = ['0'] * n
ans2 = ['0'] * n
for k in range(n):
    if a[i] < b[j]:
        ans1[i] = '1'
        i += 1
    else:
        ans2[j] = '1'
        j += 1
for i in range(n // 2):
    ans1[i] = ans2[i] = '1'
for i in range(n):
    print(ans1[i], end='')
print()
for i in range(n):
    print(ans2[i], end='')
print()
