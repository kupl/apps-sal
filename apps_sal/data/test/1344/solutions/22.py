from sys import stdin, stdout
(ins, outs) = (stdin, stdout)
n = int(ins.readline())
lst = list(map(int, ins.readline().split()))
maxi = 1
ans = 1
for i in range(1, n):
    if lst[i - 1] >= lst[i]:
        ans = max(maxi, ans)
        maxi = 0
    maxi += 1
ans = max(maxi, ans)
outs.write(str(ans))
