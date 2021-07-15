# n,m = map(int, input().split())
# sc = [map(int, input().split()) for _ in range(m)]
# s, c = [list(i) for i in zip(*sc)]
#
#
#
# for i in range(10**n):
#     ans = str(i)
#     if len(i) == n and all([i[s[j]-1] == str(c[j]) for j in range(m)]):
#         print(ans)
#         return
#
#
# print(-1)

n, m = list(map(int, input().split()))

s, c = [], []
for _ in range(m):
    s_, c_ = list(map(int, input().split()))
    s.append(s_)
    c.append(c_)

for i in range(10 ** n):
    ans = str(i)
    if len(ans) == n and all([ans[s[j] - 1] == str(c[j]) for j in range(m)]):
        print(ans)
        return

print((-1))

