res = []


def solve(Ax, A, sum=0):
    for i in range(0, Ax):
        for k in range(0, A):
            if k == 0:
                res.append(sum + A)
            else:
                res.append(sum + k)
        sum += A
    return sum


s = input().split()
N = int(s[0])
A = int(s[1])
B = int(s[2])
Ax = Bx = 0
while 1:
    if Ax * A > N:
        break
    Bx = N - Ax * A
    if Bx % B == 0:
        Bx //= B
        break
    Ax += 1
if Ax * A + Bx * B != N:
    print('-1')
else:
    solve(Bx, B, solve(Ax, A))
    print(' '.join(map(str, res)))
