n = int(input())
(s, t) = (input(), input())
a = [ord(i) - ord('a') for i in s]
b = [ord(i) - ord('a') for i in t]
(a, b, c) = (a[::-1], b[::-1], [0] * (n + 1))
for i in range(n):
    c[i] = c[i] + a[i] + b[i]
    c[i + 1] = c[i] // 26
    c[i] = c[i] % 26
c = c[::-1]
if c[0] == 0:
    c = c[1:]
ans = []
ost = 0
for digit in c:
    ost = ost * 26 + digit
    t = ost // 2
    ans.append(t)
    ost = digit % 2
if ans[0] == 0 and len(ans) > n:
    ans = ans[1:]
ans = ''.join([chr(i + ord('a')) for i in ans])
print(ans)
