import numpy as np
def resolve():
    N,A,B,C = map(int,input().split())
    Nlist = []
    YesOrNo = True
    ABC = str(input())
    for i in range(N):
        ABC_old = ABC
        if i < N-1:
            ABC = str(input())

        if ABC_old == "AB":
            if ABC == "AC":
                add1 = np.sign(B - A + 0.1)
            else:
                add1 = np.sign(B - A - 0.1)

            if add1 < 0:
                Nlist.append("B")
            else:
                Nlist.append("A")
            A = A + add1
            B = B - add1
            if A < 0 or B < 0:
                YesOrNo = False
                print('No')
                break
        
        if ABC_old == "AC":
            if ABC == "AB":
                add1 = np.sign(C - A + 0.1)
            else:
                add1 = np.sign(C - A - 0.1)

            if add1 < 0:
                Nlist.append("C")
            else:
                Nlist.append("A")
            A = A + add1
            C = C - add1
            if A < 0 or C < 0:
                YesOrNo = False
                print('No')
                break
        
        if ABC_old == "BC":
            if ABC == "AB":
                add1 = np.sign(C - B + 0.1)
            else:
                add1 = np.sign(C - B - 0.1)

            if add1 < 0:
                Nlist.append("C")
            else:
                Nlist.append("B")
            B = B + add1
            C = C - add1
            if B < 0 or C < 0:
                YesOrNo = False
                print('No')
                break

    if YesOrNo:
        print("Yes")
        s_Nlist = '\n'.join(Nlist)
        print(s_Nlist)
resolve()
