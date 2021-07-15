N = int(input())
times = list(map(int, input().split()))

M = int(input())
drinks = [tuple(map(int, input().split()))
          for _ in range(M)]

time_sum_raw = sum(times)
for pi, xi in drinks:
    print((time_sum_raw - times[pi - 1] + xi))

