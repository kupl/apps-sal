n = int(input())
s1 = 0
s2 = 0
b = False
for i in range(n):
    (x, y) = map(int, input().split())
    if x % 2 != y % 2:
        b = True
    s1 += x % 2
    s2 += y % 2
if s1 % 2 == 0 and s2 % 2 == 0:
    print(0)
elif s1 % 2 == s2 % 2 and b:
    print(1)
else:
    print(-1)
