n = int(input())
a = [int(i) for i in input().split()]
m = min(a)
f = 1
for i in a:
    if i % m != 0:
        print(-1)
        f = 0
        break
if f == 1:
    print(m)
