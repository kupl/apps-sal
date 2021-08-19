import itertools
(N, M) = map(int, input().split())
li = []
for i in range(N):
    li.append([-1 for i in range(N)])
for i in range(M):
    (a, b) = map(int, input().split())
    li[a - 1][b - 1] = 1
    li[b - 1][a - 1] = 1
an = 0
for i in itertools.permutations(range(1, N)):
    jun = [0]
    jun += list(i)
    st = jun[0]
    for t in range(1, N):
        if li[jun[t]][st] == -1:
            break
        st = jun[t]
        if t == N - 1:
            an += 1
print(an)
