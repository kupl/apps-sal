import sys
## io
IS = lambda: sys.stdin.readline().rstrip()
II = lambda: int(IS())
MII = lambda: list(map(int, IS().split()))
MIIZ = lambda: list(map(lambda x: x-1, MII()))
## dp
INIT_VAL = 0
MD2 = lambda d1,d2: [[INIT_VAL]*d2 for _ in range(d1)]
MD3 = lambda d1,d2,d3: [MD2(d2,d3) for _ in range(d1)]
## math
DIVC = lambda x,y: -(-x//y)
DIVF = lambda x,y: x//y

def main():
    n, p = MII()
    s = list(map(int, IS()))
    if 10%p == 0: # pが2または5の場合
        cnt = 0
        for i, si in enumerate(s):
            if si%p == 0:
                cnt += i+1
        print(cnt)
        return None

    d = [0]*p
    d[0] = 1 # 0(mod p)はそれ単体で割り切れるため+1しておく
    ss = 0
    x = 1
    for si in s[::-1]:
        ss += x*si
        ss %= p
        d[ss] += 1
        x = (10*x)%p # %p無しだとTLE
    cnt = 0
    for di in d:
        cnt += di*(di-1)//2 # calc combination(n_C_2)
    print(cnt)


def __starting_point():
    main()
__starting_point()
