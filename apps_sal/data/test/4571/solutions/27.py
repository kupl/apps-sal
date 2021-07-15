#78 C - HSI
N,M = map(int,input().split())
# 全て AC となる確率
p = (1/2)**M

# E = 1/p になる
E = 1/p
ans = (1900*M + 100*(N-M))*E
ans = round(ans)
print(ans)
