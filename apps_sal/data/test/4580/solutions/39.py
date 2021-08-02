N = int(input())
rate = list(map(int, input().split()))
cnt = 0
ans = []
for i in range(N):
    if rate[i] >= 3200:
        cnt += 1
    else:
        ans.append(rate[i] // 400)
s_ans = set(ans)
print(max(len(s_ans), 1), len(s_ans) + cnt)
