from collections import defaultdict

n = int(input())
A = [int(input()) for _ in range(n)]

dic = defaultdict()

for i in range(n):
    dic[i + 1] = A[i]

cnt, idx = 1, 0
val = dic[1]

while idx <= n:
    if val == 2:
        print(cnt)
        return
    val = dic[val]
    cnt += 1
    idx += 1
print((-1))
