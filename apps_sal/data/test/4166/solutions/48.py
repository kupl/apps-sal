N, M = map(int, input().split())
SC = [list(map(int, input().split())) for _ in range(M)]

if N == 1:
    start = 0
else:
    start = 10**(N - 1)
for i in range(start, 10**N):
    str_i = str(i)
    for s, c in SC:
        if str_i[s - 1] != str(c):
            break
    else:
        print(i)
        break
else:
    print(-1)
