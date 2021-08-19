with open(0) as f:
    (N, *A) = map(int, f.read().split())
A.sort(reverse=True)
Alice = sum(A[::2])
Bob = sum(A[1::2])
print(Alice - Bob)
