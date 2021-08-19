N = int(input())
(T, A) = list(map(int, input().split()))
H = list(map(int, input().split()))
k = 0
for i in range(N):
    if abs(T - 0.006 * H[i] - A) < abs(T - 0.006 * H[k] - A):
        k = i
print(k + 1)
