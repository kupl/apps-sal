S = int(input())
a = [0] * (S + 1)
a[0] = 1
for i in range(3, S + 1):
    a[i] = (a[i - 1] + a[i - 3]) % (10**9 + 7)
if S == 0:
    print((0))
else:
    print((a[S]))
