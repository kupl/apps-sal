n = int(input())
a = list(map(int, input().split()))
for i in range(n):
    a[i] -= 1
    a[i] = a[i] % 2
win = a[0] % 2
print(2 - win)
for i in range(1, n):
    if a[i]:
        win ^= 1
    print(2 - win)
