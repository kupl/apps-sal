(n,k,q) = map(int,input().split())
level = list(map(int,input().split()))
qt=[]
qid=[]
lfr = set()

for i in range(0,q):
    (qtemp,qidtemp) = map(int,input().split())
    if (qtemp == 1):
        if (len(lfr)<k):
            lfr.add(qidtemp)
        else:
            minn = qidtemp
            for el in lfr:
                if (level[el-1] < level[minn-1]):
                    minn = el
            if (level[minn-1] != level[qidtemp-1]):
                lfr.remove(minn)
                lfr.add(qidtemp)
    if (qtemp == 2):
        if (qidtemp in lfr):
            print("YES")
        else:
            print("NO")
