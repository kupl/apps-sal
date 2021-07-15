import numpy as np
def matrix_power(Mat, n):
    if n == 0:
        return I#(単位元）
    x = matrix_power(Mat, n>>1)#半分を考える
    x = np.dot(x, x)#n//2を二回行う
    if not n&1:
        return x%M
    x = np.dot(x, Mat)#あまりの分
    return x%M
I = np.identity(3, dtype = 'object') 
L, A, B, M = map(int,  input().split())
ans = np.array([[0],
                          [A],
                          [1]], dtype = 'object')
s_L = A+B*(L-1)
for digit in range(len(str(A)), len(str(s_L))+1):
    cnt = (min(s_L, 10**digit-1)-A)//B-max(-1, (10**(digit-1)-1-A)//B)
    Mat = np.array([[10**digit, 1, 0],
                            [0, 1, B],
                            [0, 0, 1]])
    ans = np.dot(matrix_power(Mat, cnt), ans)%M
print(ans[0, 0])
