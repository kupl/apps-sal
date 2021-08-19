h, w = list(map(int, input().split()))
a = [input() for _ in range(h)]
ans = ['#' * (w + 2)]
# print(ans)
for i in range(h):
    ans.append('#' + a[i] + '#')

ans.append('#' * (w + 2))
for i in range(h + 2):
    print((ans[i]))
