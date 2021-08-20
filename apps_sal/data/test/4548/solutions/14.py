(N, M, X) = map(int, input().split())
Ai = list(map(int, input().split()))
goto_0 = 0
goto_N = 0
for i in range(X, 0, -1):
    if i in Ai:
        goto_0 += 1
for i in range(X, N):
    if i in Ai:
        goto_N += 1
print(min(goto_0, goto_N))
