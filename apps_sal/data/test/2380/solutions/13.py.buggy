import math

n, m = map(int, input().split(" "))
aL = sorted(list(map(int, input().split(" "))))
bcL = sorted([list(map(int,
                       input().split(" "))) for _ in range(m)],
             key=lambda x: x[1],
             reverse=True)

csl = 0
for cnt, point in bcL:
    for i in range(cnt):
        if csl == n or aL[csl] >= point:
            print(sum(aL))
            return
        aL[csl] = point
        csl += 1

print(sum(aL))
return
