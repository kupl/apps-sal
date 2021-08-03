N = int(input())
s = []
nin = 10**7
for i in range(N):
    temp = int(input())
    if temp % 10 != 0:
        nin = min(nin, temp)
    s.append(temp)

ans = sum(s)
if ans % 10 == 0:
    ans -= nin
    print((max(ans, 0)))
else:
    print(ans)
