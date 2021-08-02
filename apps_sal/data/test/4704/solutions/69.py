from itertools import accumulate

n = int(input())
A = list(map(int, input().split()))
AA = list(accumulate([0] + A))
ans = 10 ** 20
for i in range(1, n):
    temp1 = AA[i]
    temp2 = AA[-1] - temp1
    delta = abs(temp1 - temp2)
    ans = min(delta, ans)
print(ans)
