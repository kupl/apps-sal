n = int(input())
s = input()

cnt = 0
for i in range(2, n // 2 + 1):
    if s[:i] == s[i:i + i]:
        cnt = i

if cnt == 0:
    print(n)
else:
    print(n - (cnt - 1))
