L, R = map(int, input().split())

# 例：L=3000, R=10000 で考える
# (i,j)=(3000,3001)から始まり、(3000,5018)で最小(=0)

# R-L>=2019 のとき、(L,L+1),...,(L,L+2019)の間で最小値0を取れるので、高々2018回の探索
# 全探索しても break すれば間に合う！
m = 2019
flag = False
for i in range(L, R):
    for j in range(i + 1, R + 1):
        m = min(m, i * j % 2019)
        if m == 0:
            flag = True
            break
    if flag:
        break

print(m)
