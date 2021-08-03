# https://atcoder.jp/contests/abc135/submissions/7969271
# 写経

def main():
    K = int(input())
    X, Y = map(int, input().split())

    if K % 2 == 0 and (X + Y) % 2 != 0:
        print(-1)
        return

    def next_vec(x, y):
        # 原点からx,yを目指すとき
        if x < 0:
            dx, dy = next_vec(-x, y)
            return -dx, dy
        if y < 0:
            dx, dy = next_vec(x, -y)
            return dx, -dy
        if x < y:
            dx, dy = next_vec(y, x)
            return dy, dx
        # 1手
        if x + y == K:
            return x, y
        # 2手...(1)
        if x + y <= K + K and (x + y) % 2 == 0:
            return (x + y) // 2, (x + y) // 2 - K
        # 3手以上
        return K, 0

    x, y = 0, 0
    ans = []
    while (x, y) != (X, Y):
        dx, dy = next_vec(X - x, Y - y)
        x += dx
        y += dy
        ans.append('{} {}'.format(x, y))

    print(len(ans))
    print(*ans, sep='\n')


def __starting_point():
    main()


"""
写経して計算の意味を考えた

(1)
x+y=D<2K
2手要する
S(A,B)->M(?,?)->G(X,Y)
S->M: 距離K未満=D-K詰め
M->G: 距離K詰め

S,Gから等距離Lの点M'
M'からGから離れる方向に距離Fの点M
SM'=M'G: 距離L
MM': 距離F

S->M'->M->M'->G
(S->M'->M)->M'->G: 初手
S->M': Gに距離L近づく
M'->M: Gから距離F離れる
dD_1=L-F=D-K...1

S->M'->(M->M'->G): 次手
M->M': Gに距離F近づく
M'->G: Gに距離L近づく
dD_2=L+F=K...2

1,2の連立で
L=D/2<K
F=K-D/2...(1)と符合逆だがこれは大きさ

SからGに向かって
L=D/2近づき
F離れることは可能か？
D=x+y
x>=yとすると
2D=2(x+y)<=2(2x)
D<=2x
D/2<=x
x,y方向の離れている距離のうちより離れている方向xでは
距離D/2以上離れているので、
この方向でSからGに向かってL=D/2近づくこと(=Mに到達)はできる
その後、y方向でMからGに向かうのと逆方向に
F=K-D/2進めば
次にGに向かって最短経路を進むと
距離KでGに到達できるようなM'に到達できる
"""

__starting_point()
