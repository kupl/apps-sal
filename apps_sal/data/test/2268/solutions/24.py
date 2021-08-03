n, m = map(int, input().split())
s = input()
w = list(range(26))
for i in range(m):
    a, b = input().split()
    c, d = ord(a) - ord('a'), ord(b) - ord('a')
    w[c], w[d] = w[d], w[c]
t = {chr(w[c] + ord('a')): chr(c + ord('a')) for c in range(26)}
for c in s:
    print(t[c], end="")
print()
