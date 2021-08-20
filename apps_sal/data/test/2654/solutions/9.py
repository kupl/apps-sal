import statistics
N = int(input())
AB = [map(int, input().split()) for _ in range(N)]
(A, B) = [list(i) for i in zip(*AB)]
if N % 2 == 1:
    low_med = statistics.median(A)
    high_med = statistics.median(B)
    print(high_med - low_med + 1)
else:
    low_med = statistics.median(A)
    high_med = statistics.median(B)
    print(int(2 * (high_med - low_med) + 1))
