from itertools import permutations
ls = [int(input()) for _ in range(5)]
ans = 1000000
for p in permutations(ls):
    t = 0
    for x in p[:-1]:
        t += x
        if t % 10 != 0:
            t += 10 - t % 10
    t += p[-1]
    ans = min(ans, t)
print(ans)
