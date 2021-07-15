import numpy as np
H,W = map(int,input().split())
N = int(input())
lsa = list(map(int,input().split()))
ls2 = []
for i in range(N):
    ls2 += [i+1]*lsa[i]
arr = np.array(ls2)
arr = arr.reshape(H,W).tolist()
arr2 = []
for i in range(H):
    if i % 2 == 0:
        arr2.append(arr[i])
    else:
        arr[i].reverse()
        arr2.append(arr[i])
for i in range(H):
    arr2[i] = [str(j) for j in arr2[i]]
    print(' '.join(arr2[i]))
