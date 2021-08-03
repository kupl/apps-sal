n = int(input())
vs = list(map(int, input().split(' ')))

rs = [0, 0]

for i in range(n - 1, -1, -1):
    rs = [
        min(vs[i] + rs[0], rs[1]),
        max(vs[i] + rs[0], rs[1])
    ]

print(sum(vs) - rs[1], rs[1])
