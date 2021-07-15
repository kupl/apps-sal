N = int(input())

def f(c):
    return 'B' if c == 'A' else 'A'

MOD = 10 ** 9 + 7

cs = [input() for _ in range(4)]
caa, cab, cba, cbb = cs
    
if N == 2 or N == 3:
    print(1)
    return

dpokanai = [0] * (N - 2)
dpoku = [0] * (N - 2)
dpokanai[0] = 1
for i in range(N - 3):
    dpokanai[i + 1] = dpokanai[i] + dpoku[i]
    dpoku[i + 1] = dpokanai[i]

# print(dpoku, dpokanai)

if cab == 'A':
    if caa == 'B':
        if cba == 'B':
            print(pow(2, N - 3, MOD))
        else:
            print((dpokanai[-1] + dpoku[-1]) % MOD)
    else:
        print(1)
if cab == 'B':
    if cbb == 'A':
        if cba == 'A':
            print(pow(2, N - 3, MOD))
        else:
            print((dpokanai[-1] + dpoku[-1]) % MOD)
    else:
        print(1)
