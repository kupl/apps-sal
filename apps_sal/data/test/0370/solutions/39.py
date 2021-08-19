def main():
    K = int(input())
    (X, Y) = map(int, input().split())
    if K % 2 == 0 and (X + Y) % 2 != 0:
        print(-1)
        return

    def next_vec(x, y):
        if x < 0:
            (dx, dy) = next_vec(-x, y)
            return (-dx, dy)
        if y < 0:
            (dx, dy) = next_vec(x, -y)
            return (dx, -dy)
        if x < y:
            (dx, dy) = next_vec(y, x)
            return (dy, dx)
        if x + y == K:
            return (x, y)
        if x + y <= K + K and (x + y) % 2 == 0:
            return ((x + y) // 2, (x + y) // 2 - K)
        return (K, 0)
    (x, y) = (0, 0)
    ans = []
    while (x, y) != (X, Y):
        (dx, dy) = next_vec(X - x, Y - y)
        x += dx
        y += dy
        ans.append('{} {}'.format(x, y))
    print(len(ans))
    print(*ans, sep='\n')


def __starting_point():
    main()


"\n写経して計算の意味を考えた\n\n(1)\nx+y=D<2K\n2手要する\nS(A,B)->M(?,?)->G(X,Y)\nS->M: 距離K未満=D-K詰め\nM->G: 距離K詰め\n\nS,Gから等距離Lの点M'\nM'からGから離れる方向に距離Fの点M\nSM'=M'G: 距離L\nMM': 距離F\n\nS->M'->M->M'->G\n(S->M'->M)->M'->G: 初手\nS->M': Gに距離L近づく\nM'->M: Gから距離F離れる\ndD_1=L-F=D-K...1\n\nS->M'->(M->M'->G): 次手\nM->M': Gに距離F近づく\nM'->G: Gに距離L近づく\ndD_2=L+F=K...2\n\n1,2の連立で\nL=D/2<K\nF=K-D/2...(1)と符合逆だがこれは大きさ\n\nSからGに向かって\nL=D/2近づき\nF離れることは可能か？\nD=x+y\nx>=yとすると\n2D=2(x+y)<=2(2x)\nD<=2x\nD/2<=x\nx,y方向の離れている距離のうちより離れている方向xでは\n距離D/2以上離れているので、\nこの方向でSからGに向かってL=D/2近づくこと(=Mに到達)はできる\nその後、y方向でMからGに向かうのと逆方向に\nF=K-D/2進めば\n次にGに向かって最短経路を進むと\n距離KでGに到達できるようなM'に到達できる\n"
__starting_point()
