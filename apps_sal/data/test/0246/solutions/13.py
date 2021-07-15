# -*- coding: utf-8 -*-
n, s = list(map(int, input().split(' ')))
def sumd(d):
    sd = 0
    while d!=0:
        sd += d%10
        d//=10
    return sd
st, ed = 1, n
r = 0
while True:
    if st==ed:
        r = st
        break
    x = (st+ed)//2
    if x-sumd(x)<s:
        st = x+1
    else:
        ed = x
if r-sumd(r)>=s:
    print(n-r+1)
else:
    print(0)

