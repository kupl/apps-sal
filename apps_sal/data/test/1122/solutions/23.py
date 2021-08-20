(N, M) = map(int, input().split())
for i in range(M, 0, -2):
    cur_start = (M - i) // 2
    print(cur_start + 1, cur_start + i + 1)
start = M + 2
for i in range(M - 1, 0, -2):
    cur_start = start + (M - 1 - i) // 2
    print(cur_start, cur_start + i)
