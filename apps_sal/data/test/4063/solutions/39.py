n = int(input())
d = list(map(int, input().split()))

d.sort()

# Odd pattern
if n % 2 == 1:
    print((0))
# Even pattern
else:
    ml = int(n / 2) - 1
    mr = int(n / 2)
    if d[ml] == d[mr]:
        print((0))
    else:
        print((d[mr] - d[ml]))
