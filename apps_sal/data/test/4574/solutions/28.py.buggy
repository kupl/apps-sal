N = int(input())
A = list(map(int, input().split()))
A = sorted(A, reverse=True)

store = 0
big = 0

for i in range(0, N - 1):
    if store == 1:
        store = 0
    else:
        if A[i] == A[i + 1] and big == 0:
            big = A[i]
            store = 1
        elif A[i] == A[i + 1]:
            print(A[i] * big)
            return

print(0)
