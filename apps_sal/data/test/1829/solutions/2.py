n, m = list(map(int, input().split()))
a = set()
ama, amb, am2 = n, m, 0
for i in range(n):
    a.add(input())
for i in range(m):
    s = input()
    if s in a:
        ama -= 1
        amb -= 1
        am2 += 1
xtr = am2 % 2
if ama + xtr > amb:
    print("YES")
else:
    print("NO")
