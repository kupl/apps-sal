n = int(input())
a = list(map(int, input().split()))
(s, f) = map(int, input().split())
s -= 1
f -= 1
best_sum = sum(a[s:f])
best_i = 0
cur_sum = best_sum
for i in range(1, n):
    cur_sum += a[(s - i + n) % n]
    cur_sum -= a[(f - i + n) % n]
    if cur_sum > best_sum:
        best_sum = cur_sum
        best_i = i
print(best_i + 1)
