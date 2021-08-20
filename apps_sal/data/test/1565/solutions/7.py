n = int(input())
s = input()
a = [i for i in range(1, n) if s[i] != '0']
a.sort(key=lambda i: abs(i - n / 2))
ans = float('inf')
for i in a[:6]:
    ans = min(ans, int(s[:i]) + int(s[i:]))
print(ans)
