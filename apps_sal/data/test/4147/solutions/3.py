N, A, B, C = map(int, input().split())
L_list = [int(input()) for i in range(N)]

INF = 10 ** 9


def dfs(a, b, c, n):
    if n == N:
        return abs(A - a) + abs(B - b) + abs(C - c) - 30 if min(a, b, c) > 0 else INF

    ret1 = dfs(a, b, c, n + 1)
    ret2 = dfs(a + L_list[n], b, c, n + 1) + 10
    ret3 = dfs(a, b + L_list[n], c, n + 1) + 10
    ret4 = dfs(a, b, c + L_list[n], n + 1) + 10
    return min(ret1, ret2, ret3, ret4)


ans = dfs(0, 0, 0, 0)
print(ans)
'''
8 100 90 80
100
100
90
90
90
80
80
80

0


8 1000 800 100
300
333
400
444
500
555
600
666

243

'''
