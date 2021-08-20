n = int(input())
(s, t) = map(str, input().split())
a = []
for i in range(n):
    a.append(s[i] + t[i])
a = ''.join(a)
print(a)
