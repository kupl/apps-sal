def f():
    return map(int, input().split())


(N, X) = f()
(*A,) = f()
B = [a if a <= X else X for a in A]
c = sum(A) - sum(B)
for i in range(N - 1):
    t = B[i] + B[i + 1]
    if X < t:
        d = t - X
        B[i + 1] -= d
        c += d
print(c)
