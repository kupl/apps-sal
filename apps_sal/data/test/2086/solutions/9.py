n = int(input())
A = list(map(int, input().split()))
(s, f) = list(map(int, input().split()))
s -= 1
f -= 1
m = int(1000000000.0)
best_sum = sum(A[s:f + 1])
cur_sum = best_sum
best_i = 0
for i in range(1, n):
    cur_sum += A[(s - i + n) % n]
    cur_sum -= A[(f - i + n) % n]
    if cur_sum > best_sum:
        best_sum = cur_sum
        best_i = i
print(best_i + 1)
