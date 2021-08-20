N = int(input())
guide = []
for i in range(N):
    (name, score) = map(str, input().split())
    guide.append([i, name, int(score)])
guide_sorted = sorted(guide, reverse=True, key=lambda x: x[2])
guide_sorted = sorted(guide_sorted, key=lambda x: x[1])
for i in range(N):
    print(guide_sorted[i][0] + 1)
