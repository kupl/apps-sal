import numpy as np

n,k = map(int,input().split())
a = np.array(list(map(int,input().split())))
f = np.array(list(map(int,input().split())))

a.sort();f.sort();f = f[::-1]

def test(x):
    return np.maximum(0,a-x//f).sum() <= k

def nibutan(low,hi):
    while True:
        ave = (low+hi)//2
        #ここの条件式を問題文に合わせる
        if test(ave):
            hi = ave
        else:
            low = ave
        if hi - low == 1:
            break
    li = [low,hi]
    return li

li = nibutan(-1,10**12)

print(li[1])
