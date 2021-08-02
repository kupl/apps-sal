n, a, b = map(int, input().split())
s = list(map(int, input().split()))
sm = sum(s)
s0 = s.pop(0)
s = sorted(s)
for i in range(n):
    if i == 0:
        if a * s0 / sm >= b:
            print(0)
            break
    else:
        sm -= s[-i]
        if a * s0 / sm >= b:
            print(i)
            break
