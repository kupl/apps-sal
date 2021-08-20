n = int(input())
w = [int(k) for k in input().split()]
for i in range(n):
    w[i] = [i + 1, w[i], 0]
w.sort(key=lambda e: e[1])
nextIntro = 0
result = [0 for _ in range(2 * n)]
unfilled = []
for (index, v) in enumerate(input()[:2 * n]):
    if v == '0':
        result[index] = w[nextIntro][0]
        unfilled.append(nextIntro)
        nextIntro += 1
    elif v == '1':
        result[index] = w[unfilled.pop()][0]
print(*result)
