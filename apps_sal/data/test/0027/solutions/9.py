n = int(input())
s = input()
imp = 0
for i in range(n // 2, 0, -1):
    if s[:i] == s[i:2 * i]:
        imp = i
        break
print(min(n, n - imp + 1))
