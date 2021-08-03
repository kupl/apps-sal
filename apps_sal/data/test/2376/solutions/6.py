N, W = map(int, input().split())

w1, v1 = map(int, input().split())
stuff = [[] for _ in range(4)]
stuff[0].append(v1)

for _ in range(N - 1):
    w, v = map(int, input().split())
    stuff[w - w1].append(v)

for i in stuff:
    i.sort(reverse=True)

ans = 0

for a in range(len(stuff[0]) + 1):
    for b in range(len(stuff[1]) + 1):
        for c in range(len(stuff[2]) + 1):
            for d in range(len(stuff[3]) + 1):

                if a * w1 + b * (w1 + 1) + c * (w1 + 2) + d * (w1 + 3) <= W:
                    ans = max(ans, sum(stuff[0][:a]) + sum(stuff[1][:b]) + sum(stuff[2][:c]) + sum(stuff[3][:d]))

print(ans)
