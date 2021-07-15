n = int(input())
l = [list(map(int, input().split())) for _ in range(2)]

r1 = []
tmp1 = 0
for i in range(n):
    rui1 = l[0][i] + tmp1
    r1.append(rui1)
    tmp1 = rui1

r2 = [0] * n
tmp2 = 0
for i in reversed(range(n)):
    rui2 = l[1][i] + tmp2
    r2[i] = rui2
    tmp2 = rui2

max_cnt = 0
for i in range(n):
    cnt = r1[i] + r2[i]
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
