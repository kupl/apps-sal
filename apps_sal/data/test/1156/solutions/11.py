n = int(input())
a = list(map(int, input().split()))
b = input()
r = 1000000000.0
l = -1000000000.0
for i in range(4, n):
    if b[i - 4:i] == '1111' and b[i] == '0':
        r = min(r, min(a[i - 4:i + 1]) - 1)
    if b[i - 4:i] == '0000' and b[i] == '1':
        l = max(l, max(a[i - 4:i + 1]) + 1)
print(int(l), int(r))
