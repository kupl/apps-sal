
n = int(input())
vals = [tuple(int(v) for v in input().split()) for _ in range(n)]

other = [(p, i) for i, (a, p) in enumerate(vals)]
other.sort()

last = n
ans = 0

for p, i in other:
    if i > last:
        continue
    ans += sum(a for a, pp in vals[i:last]) * p
    last = i
    if last == 0:
        break

print(ans)
