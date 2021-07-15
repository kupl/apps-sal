import numpy as np

n = int(input())
v = np.array(list(map(int,input().split())))
c = np.array(list(map(int,input().split())))
a = v-c
print((a[a>=0].sum()))

