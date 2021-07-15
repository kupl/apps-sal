#B
def is_belong(A, C, x, y):
    return A*x + y + C == 0

def solution():
    n = int(input())
    a = [int(i) for i in input().split()]

    #if n == 3:
    #    print('Yes')
    #    return
    
    other_pointes_indexes = []
    for k in [0, 1]:
        #зададим прямую по двум точкам
        for i in range(1, n):
                if k == i:
                    continue
                #использовала уравнение Ax + y + C = 0
                #A = (y2 - y1)/(x1 - x2)
                #C = -y1 - Ax1
                A = 0
                if k - i != 0:
                    A = (a[i] - a[k])/(k - i)
                C1 = -a[k] - A*k
                C2 = C1
                
                #проверяем принадлежность точек прямым
                success = True
                for j in range(n):
                    if not is_belong(A, C1, j, a[j]):
                        if C2 != C1:
                            if not is_belong(A, C2, j, a[j]):
                                success = False
                                break
                        else:
                            C2 = -A*j - a[j]
                if success:
                    if C1 != C2:
                        print('Yes')
                        return
            
    print('No')
    
solution()
