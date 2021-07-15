N = int(input())
A = [int(input()) for i in range(N)]

max_v, next_max_v = sorted(A, reverse=True)[:2]
for a in A:
    print(max_v if a != max_v else next_max_v)
