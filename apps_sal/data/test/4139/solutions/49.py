import sys
sys.setrecursionlimit(10**6)
n=int(input())
def res(v:int, all:list):
    if v>n:
        return
    if "3" in list(str(v)) and "5" in list(str(v)) and "7" in list(str(v)):
        all.append(v)
    res(10*v+3,all)
    res(10*v+5,all)
    res(10*v+7,all)
all=[]

res(3,all)
res(5,all)
res(7,all)


print(len(all))
