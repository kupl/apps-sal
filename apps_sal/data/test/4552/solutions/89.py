N = int(input())
F = [list(map(int, input().split())) for _ in range(N)]
P = [list(map(int, input().split())) for _ in range(N)]

max_prof = -float('inf')

for s in range(1, 1 << 10):

    sum_prof = 0
    for store_no in range(N):
        state = s

        time_zone = 0
        both_open_cnt = 0
        while state > 0:
            if (state & 1) and F[store_no][time_zone]:
                both_open_cnt += 1

            state >>= 1
            time_zone += 1

        sum_prof += P[store_no][both_open_cnt]

    max_prof = max(max_prof, sum_prof)


print(max_prof)
