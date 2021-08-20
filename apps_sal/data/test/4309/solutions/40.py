N = list(input())
n = int(''.join(N))
ck = int(N[0] * 3)
if n - ck <= 0:
    print(int(N[0] * 3))
else:
    print(int(str(int(N[0]) + 1) * 3))
pass
