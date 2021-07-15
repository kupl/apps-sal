import sys
input = sys.stdin.readline


N = int(input())
graph = [[] for _ in range(N)]
P = list(map(int, input().split()))
Xs = list(map(int, input().split()))

for i, p in enumerate(P):
    graph[p-1].append(i+1)

stack = [0]
Scores = [[0, 0] for _ in range(N)]
Ind = [0]*N
ok = True
while stack and ok:
    p = stack[-1]
    if Ind[p] == len(graph[p]):
        stack.pop()
        Max = Xs[p]
        dp = [False]*(Max+1)
        dp[0] = True
        S = 0
        for ch in graph[p]:
            a, b = Scores[ch]
            S += a+b
            for x in reversed(range(Max+1)):
                dp[x] = (x >= a and dp[x-a]) or (x >= b and dp[x-b])
        to_ret = -1
        for x in reversed(range(Max+1)):
            if dp[x]:
                to_ret = S - x
                break
        if to_ret == -1:
            ok = False
        else:
            Scores[p] = [Max, to_ret]
    else:
        stack.append(graph[p][Ind[p]])
        Ind[p] += 1

print("POSSIBLE" if ok else "IMPOSSIBLE")
