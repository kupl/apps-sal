import sys
sys.setrecursionlimit(10**7)


def main():
    N, M = list(map(int, input().split()))
    V = [[] for _ in range(N)]
    for _ in range(M):
        a, b = list(map(int, input().split()))
        V[a - 1].append(b - 1)
    C = [0] * N
    loop = []

    def dfs(n):
        if C[n] == 2:
            return False
        if C[n] == 1:
            loop.append(n)
            return True
        C[n] = 1
        for i in V[n]:
            if dfs(i):
                loop.append(n)
                return True
        C[n] = 2
        return False
    for i in range(N):
        if dfs(i):
            break
    if len(loop) == 0:
        print('-1')
        return
    for i in range(1, len(loop)):
        if loop[i] == loop[0]:
            break
    loop = loop[:i][::-1]

    def minimize(l):
        s = set(l)
        for i in range(len(l)):
            for j in V[l[i]]:
                if j == l[(i + 1) % len(l)]:
                    continue
                if j in s:
                    break
            else:
                continue
            break
        else:
            return l
        I = {m: k for k, m in enumerate(l)}
        j = I[j]
        if i < j:
            l = l[0:i + 1] + l[j:]
        else:
            l = l[j:i + 1]
        return l
    while True:
        t = len(loop)
        loop = minimize(loop)
        if len(loop) == t:
            break
    print(t)
    print(('\n'.join(str(i + 1) for i in loop)))


main()
