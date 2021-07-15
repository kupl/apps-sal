k, n = list(map(int, input().split()))
j = list(map(int, input().split()))
b = list(map(int, input().split()))

b_set = set(b)
my_sum = [0 for i in range(k)]
my_sum[0] = j[0]

for i in range(1, k):
    my_sum[i] = my_sum[i - 1] + j[i]

pos_val = set()
for score in my_sum:
    pos_val.add(b[0] - score)

ans = 0
for start_val in pos_val:
    score_set = set()
    for marks in my_sum:
        score = start_val + marks
        score_set.add(score)

    if (score_set & b_set) == b_set:
        ans += 1

print(ans)

