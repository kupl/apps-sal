
n = int(input())
bs = list(map(int, input().split()))

assert(len(bs) == n)

bs = sorted(bs)

last = -1
cost = 0
for b in bs:
    if b <= last:
        diff = last - b
        b += diff + 1
        cost += diff + 1
    last = b

print(cost)
