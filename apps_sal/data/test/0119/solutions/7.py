n = int(input())
a = []
for i in range(n):
    a.append(list(map(int, input().split())) + [i])
a.sort(key=lambda f: (f[0], -f[1]))
for i in range(n - 1):
    if a[i][1] >= a[i + 1][1]:
        print(a[i + 1][2] + 1, a[i][2] + 1)
        break
else:
    print(-1, -1)
