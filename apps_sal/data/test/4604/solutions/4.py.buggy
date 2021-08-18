n = int(input())
a = sorted(list(map(int, input().split())))
ans = 1

if n % 2 == 0:
    for i in range(0, n, 2):
        if a[i] != i + 1 or a[i + 1] != i + 1:
            print(0)
            return
else:
    if a[0] != 0:
        print(0)
        return
    for i in range(1, n, 2):
        if a[i] != i + 1 or a[i + 1] != i + 1:
            print(0)
            return

for i in range(n // 2):
    ans = ans * 2 % (10**9 + 7)

print(ans)
