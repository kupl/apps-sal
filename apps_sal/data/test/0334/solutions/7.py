import sys
a, b = list(map(int, input().split()))
c, d = list(map(int, input().split()))
s = set()
for i in range(1001):
    s.add(b + i * a)
for i in range(1000):
    num = d + c * i
    if num in s:
        print(num)
        return
print(-1)
