n = int(input())
a = list(map(int, input().split()))
a.sort()
res = True
if n % 2 != 0:
    if a[0] != 0:
        res = False
        print(0)
    a = a[1:]
for i in range(0, len(a), 2):
    if a[i] != a[i + 1]:
        print(0)
        res = False
        break
p = 10 ** 9 + 7
if res:
    print(pow(2, n // 2, p))
