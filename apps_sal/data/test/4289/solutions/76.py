N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))

diff = 100000009
diff_id = 0
for i in range(N):
    if diff > abs(A - (T - H[i] * 0.006)):
        diff = abs(A - (T - H[i] * 0.006))
        diff_id = i

print(diff_id + 1)
