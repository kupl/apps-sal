n = int(input())
P = list(map(int, input().split()))
S = list(input())
a_sum = 0
b_sum = 0
for i in range(n):
    if S[i] == 'A':
        a_sum += P[i]
    else:
        b_sum += P[i]
max_b = b_sum
b_sum_copy = b_sum
for i in range(n):
    if S[i] == 'A':
        b_sum += P[i]
    else:
        b_sum -= P[i]
    max_b = max(max_b, b_sum)
b_sum = b_sum_copy
for i in range(n - 1, -1, -1):
    if S[i] == 'A':
        b_sum += P[i]
    else:
        b_sum -= P[i]
    max_b = max(max_b, b_sum)
print(max_b)
