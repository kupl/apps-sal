import numpy as np
s = input()
effects = [1, 10, 9, 12, 3, 4]
mod = 10**9+7

amari = np.array([1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
arrays = [np.eye(13, k=i, dtype=np.int64)+np.eye(13, k=i-13, dtype=np.int64) for i in range(13)]
brrays = [sum(arrays[c*effects[i]%13] for c in range(10)) for i in range(6)]
for i, c in enumerate(reversed(s)) :
    if c != "?" :
        c = int(c)
        array = arrays[c*effects[i%6]%13]
        amari = np.dot(amari, array)
    else :
        array = brrays[i%6]
        amari = np.dot(amari, array)%mod

print(amari[5])
