import math
import bisect
import itertools
import decimal

def ria():
    return [int(i) for i in input().split()]

st=set()
mx=0
n=ria()[0]

ar=ria()
for i in ar:
    if i not in st:
        st.add(i)
    else:
        st.remove(i)
    mx=max(len(st),mx)
print(mx)
