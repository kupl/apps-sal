import numpy as np

N = input().split()
N = (int)(N[0])
A = np.array(list(map(int, input().split())))

s = 0
I = np.array([i+1 for i in range(N)])
Aminusi = np.array(A-I)


mmid = np.median(Aminusi)

sad = 0
for l in Aminusi :
    sad += abs(l-mmid)

print((int(sad)))


