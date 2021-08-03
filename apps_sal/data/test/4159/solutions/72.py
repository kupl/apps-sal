a, b, k = map(int, input().split())

a_ans = max(0, a - k)
b_ans = max(0, b - max(0, k - a))

print(a_ans, b_ans)
