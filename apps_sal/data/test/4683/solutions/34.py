def cin():
    return list(map(int, input().split()))


N = int(input())
A = cin()

total = 0
store = 0
for i in range(N - 1):
    store += A[N - i - 1]
    total += A[N - i - 2] * store
print((total % (pow(10, 9) + 7)))

