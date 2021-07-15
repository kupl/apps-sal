"""http://codeforces.com/problemset/problem/864/D"""
# 17:54
def make_a_permutation():
    n = int(input())
    a = list(map(int, input().split()))
    occ = [0] * (n+1)
    for i in range(n):
        occ[a[i]] += 1
    missing = [i for i in range(1,n+1) if occ[i] == 0]
    mi = 0
    dupIndexes = [i for i in range(n) if occ[a[i]] >= 2]
    fixedNum = [False] * (n+1)
    for i in range(n):
        if occ[i] == 1:
            fixedNum[i] = True
    
    for dup in dupIndexes:
        dupNum = a[dup]
        if occ[dupNum] > 1 and (fixedNum[dupNum] or dupNum > missing[mi]):
            fixedNum[missing[mi]] = True
            occ[missing[mi]] += 1
            a[dup]= missing[mi]
            mi += 1
            occ[dupNum] -= 1
        else:
                fixedNum[dupNum] = True
    return mi, a
   
c, l = make_a_permutation()
print(c)
for i in range(len(l)):
    print(l[i], end=" ")

