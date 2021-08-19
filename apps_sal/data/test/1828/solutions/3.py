n = int(input())
p = []
for _ in range(n + 1):
    (x, y) = map(int, input().split())
    p.append((x, y))


def cp(v1, v2):
    return v1[0] * v2[1] - v1[1] * v2[0]


answer = 0
for i in range(n - 1):
    v1 = (p[i + 1][0] - p[i][0], p[i + 1][1] - p[i][1])
    v2 = (p[i + 2][0] - p[i + 1][0], p[i + 2][1] - p[i + 1][1])
    if cp(v1, v2) > 0:
        answer += 1
print(answer)
