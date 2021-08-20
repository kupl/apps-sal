(n, a, b) = list(map(int, input().split()))
holes = list(map(int, input().split()))
s = sum(holes)
f = holes[0]
del holes[0]
holes = sorted(holes)[::-1]
h = 0
for x in range(len(holes)):
    if f * a / s >= b:
        break
    s -= holes[x]
    h += 1
print(h)
