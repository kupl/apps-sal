n, k = list(map(int, input().split()))
s = input()
i = 1
while i < len(s) and s[i:] != s[:n - i]:
    i += 1
t = s[:i] * k + s[i:]
print(t)
