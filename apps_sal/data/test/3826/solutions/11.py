import collections
def __starting_point():
    N = int(input())
    A = [int(a) for a in input().split(" ")]
    C = collections.Counter(A)
    n_duplicate = 0
    for k, v in list(C.items()):
        if v > 1:
            n_duplicate += v - 1
    if n_duplicate == 0:
        print("0")
    else:
        ans = N
        for i in range(0, N - 1):
            T = collections.Counter(A)
            t_duplicate = n_duplicate
            for j in range(i, min(N, i + ans)):
                T[A[j]] -= 1
                if T[A[j]] >= 1:
                    t_duplicate -= 1
                if t_duplicate == 0:
                    ans = j + 1 - i
                    break
        print(str(ans))



__starting_point()
