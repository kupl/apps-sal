N = int(input())
takahashi = 1
aoki = 1
for i in range(N):
    (T, A) = list(map(int, input().split()))
    n = max((takahashi + T - 1) // T, (aoki + A - 1) // A)
    takahashi = n * T
    aoki = n * A
print(takahashi + aoki)
