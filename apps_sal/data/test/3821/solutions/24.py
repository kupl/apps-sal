n = int(input())
p = list(map(float, input().split()))
p.sort(reverse=True)
prev_prob = 0
cur_prob = 0
T = 1
for i in range(n):
    cur_prob = cur_prob * (1 - p[i]) + T * p[i]
    if cur_prob >= prev_prob:
        prev_prob = cur_prob
        T *= 1 - p[i]
    else:
        break
print(prev_prob)
