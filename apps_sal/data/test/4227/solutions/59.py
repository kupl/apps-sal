from itertools import permutations
(N, M) = map(int, input().split())
S = []
for i in range(M):
    (a, b) = map(int, input().split())
    S.append([a, b])
vertex = (i + 1 for i in range(N))
all_path = list(permutations(vertex))
ans = 0
for p in all_path:
    flag = True
    if p[0] == 1:
        for i in range(N - 1):
            if [p[i], p[i + 1]] not in S and [p[i + 1], p[i]] not in S:
                flag = False
                break
        if flag:
            ans += 1
print(ans)
