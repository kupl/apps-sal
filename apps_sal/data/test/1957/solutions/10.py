n, A, B = list(map(int, input().split()))
s = list(map(int, input().split()))
su = 0
for i in range(n):
    su += s[i]
s2 = s[1:]
we = 0
s2.sort()
s2 = s2[::-1]
kol = 0
if A * s[0] / su >= B:
    print(0)
else:
    for i in range(len(s2)):
        su -= s2[i]
        kol += 1
        if A * s[0] / su >= B:
            print(kol)
            we = 1
            break

