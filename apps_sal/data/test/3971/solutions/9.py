input()
s = [0] * 100002
for i in map(int, input().split()):
    s[i] += i
a = b = 0
for d in s:
    (a, b) = (max(a, b), a + d)
print(a)
