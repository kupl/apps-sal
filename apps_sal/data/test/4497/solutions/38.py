N = int(input())
lis = [0] * (N + 1)
Mcnt = 0
Mi = 1
for i in range(1, N + 1):
    lis[i] = i
    cnt = 0
    while lis[i] % 2 == 0:
        lis[i] //= 2
        cnt += 1
    if Mcnt < cnt:
        Mcnt = cnt
        Mi = i
print(Mi)
