n = int(input())
w = list(map(int, input().split()))
w_len = len(w)
ans = []
for t in range(0, w_len):
    ans.append(abs(sum(w[:t + 1]) - sum(w[t + 1:])))
print(min(ans))
