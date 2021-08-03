import statistics

N = int(input())
AB = [map(int, input().split()) for _ in range(N)]
A, B = [list(i) for i in zip(*AB)]


A_median = statistics.median(A)
B_median = statistics.median(B)
if N % 2 == 0:
    print(int((B_median - A_median) * 2) + 1)
else:
    print(B_median - A_median + 1)
