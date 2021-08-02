n = int(input())

d = []
for i in range(n):
    a, b = list(map(int, input().split()))
    d.append((a, -1))
    d.append((b, 1))

d.sort()
t = 0
for a, b in d:
    t -= b
    if t > 2:
        print("NO")
        return
print("YES")
