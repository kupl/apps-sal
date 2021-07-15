def Zs(): return list(map(int, input().split()))
def Z(): return int(input())

def solve(N, A):
    s = [0] * (N + 1)
    for i in range(N):
        s[i + 1] = s[i] + A[i]
    aru = [False] * (N + 1)
    for i in range(N):
        for j in range(i + 1, N):
            if s[j + 1] - s[i] <= N:
                aru[s[j + 1] - s[i]] = True
    ans = 0
    for i in range(N):
        if aru[A[i]]: ans += 1
    return ans

for _ in range(Z()):
    N = Z()
    A = Zs()
    print(solve(N, A))



