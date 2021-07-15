TOT = 2*10**5
# print(TOT)
a = [-1] * (TOT + 1)

q = int(input())
fp = input().split()
a[int(fp[1])] = 0
L = -1
R = 1
for _ in range(q-1):
    qq = input().split()
    pos = int(qq[1])
    if (qq[0]=='L'):
        a[pos] = L
        L -= 1
    elif qq[0]=='R':
        a[pos] = R
        R += 1
    else:
        print(min(a[pos] - L - 1,R - a[pos] - 1))
        

