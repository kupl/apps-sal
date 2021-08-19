N = int(input())
a = list(map(int, input().split()))
ans = [0 for i in range(9)]
for i in range(N):
    temp = a[i] // 400
    if temp > 8:
        ans[8] += 1
    else:
        ans[temp] += 1
nin = 0
for i in range(8):
    if ans[i] != 0:
        nin += 1
if nin == 0 and ans[8] != 0:
    nin += 1
    nax = ans[8]
else:
    nax = nin + ans[8]
print(nin, nax)
