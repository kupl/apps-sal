N, A, B, C = map(int, input().split())
l = []
for i in range(N):
    l.append(int(input()))


def dfs(bamboo, a, b, c):
    if bamboo == N:
        if min(a, b, c) > 0:
            return abs(A - a) + abs(B - b) + abs(C - c) - 30
        else:
            return 10**10
    else:
        ans1 = dfs(bamboo + 1, a, b, c)
        ans2 = dfs(bamboo + 1, a + l[bamboo], b, c) + 10
        ans3 = dfs(bamboo + 1, a, b + l[bamboo], c) + 10
        ans4 = dfs(bamboo + 1, a, b, c + l[bamboo]) + 10
        return min(ans1, ans2, ans3, ans4)


print(dfs(0, 0, 0, 0))
