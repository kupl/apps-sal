n = int(input())
s5 = 0
s0 = 0
ar = list(input().split())
for i in range(n):
    if ar[i] == '5':
        s5 += 1
    else:
        s0 += 1
while s5 % 9 and s5:
    s5 -= 1
if s5 and s0:
    print(s5*'5' + '0'*s0)
elif s0:
    print(0)
else:
    print(-1)
