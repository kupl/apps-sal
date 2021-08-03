N = int(input())
T, A = 1, 1
for _ in range(N):
    t, a = map(int, input().split())
    k = max((T - 1) // t + 1, (A - 1) // a + 1)
    T = t * k
    A = a * k
print(A + T)
