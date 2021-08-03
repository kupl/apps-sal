n = int(input())

tmp_h = [False] * (n + 1)
tmp_v = [False] * (n + 1)

answer = []
for i in range(1, n**2 + 1):
    h, v = map(lambda x: int(x) - 1, input().split())
    if not tmp_h[h] and not tmp_v[v]:
        tmp_h[h] = True
        tmp_v[v] = True
        answer.append(i)

print(' '.join(map(str, answer)))
