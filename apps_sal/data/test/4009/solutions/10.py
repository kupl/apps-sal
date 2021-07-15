n, x, y = map(int, input().split())
s = input()
count = 0
for i in range(n - x, n):
    if s[i] == "1" and i != n - y - 1:
        count += 1
    if s[i] == "0" and i == n - y - 1:
        count += 1
print(count)
