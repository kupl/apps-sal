n = int(input())
a = list(map(int, input().split()))

res = 0

for i in range(n):
    if a[i] == i:
        res += 1

for i in range(n):
    if a[i] != i and a[a[i]] == i:
        res += 2
        print(res)
        return

if res != n:
    res += 1

print(res)
