import itertools
(N, M) = map(int, input().split())
leng = [set() for i in range(N + 1)]
res = 0
for _ in range(M):
    (a, b) = map(int, input().split())
    leng[a].add(b)
    leng[b].add(a)


def check(arr):
    for i in range(N - 1):
        if arr[i + 1] not in leng[arr[i]]:
            return False
    return True


for i in itertools.permutations([x for x in range(2, N + 1)]):
    if check([1] + list(i)):
        res += 1
print(res)
