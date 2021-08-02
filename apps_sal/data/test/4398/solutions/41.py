n = int(input())
s = input()
s = s.split()
t = list(s[1])
s = list(s[0])
a = s[0] + t[0]
for b in range(n - 1):
    a = a + s[b + 1]
    a = a + t[b + 1]
print(a)
