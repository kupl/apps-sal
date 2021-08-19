(n, k) = map(int, input().split())
s = input()
if s[k - 1] == 'A':
    s = s[:k - 1] + 'a' + s[k:]
if s[k - 1] == 'B':
    s = s[:k - 1] + 'b' + s[k:]
if s[k - 1] == 'C':
    s = s[:k - 1] + 'c' + s[k:]
print(s)
