def Ten_to_n(X, n):
    if int(X / n):
        return Ten_to_n(int(X / n), n) + str(X % n)
    return str(X % n)


(n, k) = list(map(int, input().split()))
print(len(Ten_to_n(n, k)))
