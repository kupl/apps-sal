from sys import stdout
def printn(x): return stdout.write(str(x))
def inn(): return int(input())


def inl(): return list(map(int, input().split()))
def inm(): return list(map(int, input().split()))
def ins(): return input().strip()


DBG = True
BIG = 999999999
R = 10**9 + 7


def ddprint(x):
    if DBG:
        print(x)


a, b = inm()
c = [['
c.extend([['.'] * 50 for i in range(45)])
for z in range(a - 1):
    c[(z // 25) * 2][(z % 25) * 2]= '.'
for z in range(b - 1):
    c[(z // 25) * 2 + 50][(z % 25) * 2]= '
print('90 50')
for i in range(90):
    print((''.join(c[i])))
