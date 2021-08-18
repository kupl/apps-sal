n = int(input())
a = [0] + list(map(int, input().split())) + [1001]
max_ans = 0
ans = 0

for i in range(1, len(a) - 1):
    if a[i] == a[i - 1] + 1 and a[i] == a[i + 1] - 1:
        ans += 1
    else:
        max_ans = max(ans, max_ans)
        ans = 0

print(max(max_ans, ans))
