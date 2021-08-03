n = int(input())
p = int(input())
s = p + 1
for i in range(1, n):
    c = int(input())
    s += abs(p - c) + 2
    p = c
print(s)
