from collections import defaultdict
import sys
readline = sys.stdin.readline

N, K = map(int, readline().split())

sushi = defaultdict(list)

for i in range(N):
    t, d = map(int, readline().split())
    sushi[t].append(d)

best_sushi = []
other_sushi = []

for value in sushi.values():
    value = sorted(value, reverse=True)
    best_sushi.append(value[0])
    other_sushi += value[1:]

best_sushi = sorted(best_sushi, reverse=True)
other_sushi = sorted(other_sushi, reverse=True)


best_num = 1
other_num = K - 1

if len(other_sushi) < other_num:
    other_num = len(other_sushi)
    best_num = K - other_num


other_sushi = other_sushi[:other_num]

sushi_point = sum(best_sushi[:best_num]) + sum(other_sushi)
kind_point = best_num ** 2

ans = sushi_point + kind_point

for i in range(best_num, len(best_sushi)):
    sushi_point += best_sushi[i]
    if len(other_sushi) == 0:
        break
    rem = other_sushi.pop()
    sushi_point -= rem
    kind_point = (i + 1) ** 2

    if ans < sushi_point + kind_point:
        ans = sushi_point + kind_point

print(ans)
