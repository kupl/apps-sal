import math

def cal(H,M):

    H = 360/12*H + 1/12 * (M/60) *  360
    M = 360/60*M
    H_M = abs(H-M)

    if H_M > 180:
        H_M = 360 - H_M
    
    return H_M

def main():
    A, B, H, M = map(int,input().split())
    
    angle = cal(H,M)
    
    if angle == 180:
        print(A+B)
    
    else:
        print(math.sqrt(A*A + B*B - 2*A*B*math.cos(math.radians(angle))))
              
main()
