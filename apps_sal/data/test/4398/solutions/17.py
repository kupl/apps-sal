n = int(input())
(s, t) = map(str, input().split())
a = ''
for i in range(n):
    a = a + s[i] + t[i]
print(a)
