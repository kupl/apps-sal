n = int(input())
c = list(map(int, input().split()))
c_ans = []
ans = 0
for i in range(n):
    ans += c[i]
    c_ans.append(ans)
re_ans = 0
for i in range(n):
    re_ans += c[i] * (c_ans[n - 1] - c_ans[i])
re_ans = re_ans % (10 ** 9 + 7)
print(re_ans)
