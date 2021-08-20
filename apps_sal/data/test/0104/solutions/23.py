n = int(input())
a = list(map(int, input().split()))
s = sum(a) / 2
for i in range(n):
    s -= a[i]
    if s <= 0:
        print(i + 1)
        break
