import bisect
(X, N) = map(int, input().split())
if N == 0:
    print(X)
else:
    p = set(map(int, input().split()))
    num_list = set([i for i in range(-1, 102)])
    num_list = sorted(list(num_list ^ p))
    nummin = num_list[bisect.bisect_left(num_list, X)]
    nummax = num_list[bisect.bisect_right(num_list, X)]
    if nummin == nummax:
        nummin = num_list[bisect.bisect_left(num_list, X) - 1]
    if X - nummin <= nummax - X:
        print(nummin)
    else:
        print(nummax)
