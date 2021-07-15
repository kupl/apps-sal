n = int(input())
a = list(map(int, input().split()))
b = input()

r = 1e+9
l = -1e+9

for i in range(4, n):
    if b[i - 4: i] == "1111" and b[i] == "0":
        r = min(r, min(a[i - 4: i + 1]) - 1)
    if b[i - 4: i] == "0000" and b[i] == "1":
        l = max(l, max(a[i - 4: i + 1]) + 1)

print(int(l), int(r))

