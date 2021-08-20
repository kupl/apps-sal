from itertools import permutations
N = int(input())
arr = [list(map(int, input().split())) for i in range(N)]


def dis(x):
    c = 0
    for i in range(N - 1):
        aa = arr[x[i]][0] - arr[x[i + 1]][0]
        bb = arr[x[i]][1] - arr[x[i + 1]][1]
        c += (aa ** 2 + bb ** 2) ** 0.5
    return c


count = 0
ans = 0
for i in permutations(list(range(0, N)), N):
    count += 1
    ans += dis(i)
print(ans / count)
