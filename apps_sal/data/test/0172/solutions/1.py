n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
s = 0
for i in range(1, 6):
    x = a.count(i)
    y = b.count(i)
    if not (x + y) % 2: s += abs(x - y) // 2
    else: print(-1); return()
print(s // 2)
