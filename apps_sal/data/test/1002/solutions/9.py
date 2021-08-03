n, d = map(int, input().split(' '))
ns = list(map(int, input().split(' ')))

if d < sum(ns) + 10 * (len(ns) - 1):
    print(-1)
else:
    answer = (d - sum(ns)) // 5
    print(answer)
