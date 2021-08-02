
n = int(input())
pairs = [list(map(int, input().split())) + [i] for i in range(n)]
pairs.sort(key=lambda x: (x[0], -x[1]))
for i in range(1, n):
    if pairs[i][1] <= pairs[i - 1][1]:
        print(pairs[i][2] + 1, pairs[i - 1][2] + 1)
        break
else:
    print(-1, -1)
