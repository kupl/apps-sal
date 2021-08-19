(k, x) = map(int, input().split())
min_ans = x - k + 1
max_ans = x + k - 1
for x in range(min_ans, max_ans + 1):
    print(x, end=' ')
