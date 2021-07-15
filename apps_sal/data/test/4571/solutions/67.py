#78 C - HSI
N,M = map(int,input().split())
# 全て AC となる確率
p = (1/2)**M

# 全て AC となるときの期待値
# k 回目までに「成功しない」確率の期待値
# E = (1-p)**0 + (1-p)**1 + (1-p)**2+...
E = 0
for k in range(10**6):
    E += (1-p)**k

ans = (1900*M + 100*(N-M))*E
ans = round(ans)
print(ans)
