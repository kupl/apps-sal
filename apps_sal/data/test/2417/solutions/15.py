n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
memo = {}
for i in range(n):
    memo[a[i]] = i
ans = [0] * n
for i in range(n):
    ans[i] = memo[b[i]]
min_num = 10 ** 9
cnt = 0
for i in range(n)[::-1]:
    if ans[i] > min_num:
        cnt += 1
    min_num = min(min_num, ans[i])
print(cnt)
