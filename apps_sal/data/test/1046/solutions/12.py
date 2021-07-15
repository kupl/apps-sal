n = int(input())
s = list(map(int, input().split()))
x = set(s)

r = 0

for i in x:
    if i != 0:
        p = s.count(i)
        if p == 2:
            r += 1
        elif p > 2:
            print(-1)
            return

print(r)

