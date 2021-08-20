def Points(P, T):
    return max(3 * P / 10, P - P / 250 * T)


Inpts = list(map(int, input().split()))
if Points(Inpts[0], Inpts[2]) > Points(Inpts[1], Inpts[3]):
    print('Misha')
if Points(Inpts[0], Inpts[2]) < Points(Inpts[1], Inpts[3]):
    print('Vasya')
if Points(Inpts[0], Inpts[2]) == Points(Inpts[1], Inpts[3]):
    print('Tie')
