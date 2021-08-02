n = int(input())
s = []
for i in range(n):
    s.append(list(map(int, input().split())))
s.sort()
m = 0
for a, b in s:
    if b >= m:
        m = b
    else:
        m = a
print(m)
