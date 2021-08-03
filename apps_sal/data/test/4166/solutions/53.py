N, M = map(int, input().split())
x = [-9] + [-10] * (N - 1)
for _ in range(M):
    s, c = map(int, input().split())
    if x[s - 1] >= 0 and x[s - 1] - c:
        print(-1)
        break
    x[s - 1] = c
else:
    if x[0] == -9 and N == 1:
        print(0)
    elif x[0]:
        print(sum(x[-i - 1] % 10 * 10**i for i in range(N)))
    elif N < 2:
        print(0)
    else:
        print(-1)
