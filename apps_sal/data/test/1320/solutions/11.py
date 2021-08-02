def f(n):
    return (n * (n - 1)) // 2


n = int(input())
ver = [0] * n
gor = [0] * n
for i in range(n):
    lst = input()
    for j in range(n):
        if lst[j] == 'C':
            gor[i] += 1
            ver[j] += 1
ans = 0
for i in ver:
    ans += f(i)
for i in gor:
    ans += f(i)

print(ans)
