n = int(input())
s = []
for i in range(n):
    s.append(input())
m = int(input())
t = []
for i in range(m):
    t.append(input())
words = set(s + t)
max_val = 0
for word in words:
    ans = s.count(word)
    ans -= t.count(word)
    if ans > max_val:
        max_val = ans
print(max_val)
