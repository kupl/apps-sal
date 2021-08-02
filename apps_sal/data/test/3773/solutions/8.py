
import sys
sys.setrecursionlimit(10**7)


def main1(n, a, k):
    ret = True
    # 各山のGrundy数を求め、xor和をとる。
    # N<=200,a<=10^9,k<=10^9
    ary = [0] * n
    for i in range(n):
        if k[i] == 1:
            ary[i] = a[i]
        elif a[i] % k[i] == 0:
            ary[i] = a[i] // k[i]
        else:
            m = a[i] // k[i]
            # 0,1,..,mのいずれか
            # m+1周期になっている。
            # t=(a[i]%k[i])%(m+1)
            # 周期のidx=tの数字は何か。
            # t=0ならm
            # tをデクリメントすると、0,..,m-1のm周期上のidxになる

            def func(t, m):  # m+1周期のidx=tの値を返す。
                t %= (m + 1)
                if t == 0: return m
                j = (m + 1 - t + k[i] - 1) // k[i]
                tt = t - j
                tt += k[i] * j
                ret = func(tt, m - j)
                return ret
            t = (a[i] % k[i]) % (m + 1)
            ary[i] = func(t, m)
    ret = 0
    for x in ary: ret ^= x
    return ret > 0


def __starting_point():
    n = int(input())
    a, k = [], []
    for _ in range(n):
        x, y = list(map(int, input().split()))
        a.append(x)
        k.append(y)
    print(('Takahashi' if main1(n, a, k) else 'Aoki'))


__starting_point()
