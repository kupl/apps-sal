from heapq import heappush, heappop

def readinput():
    n,m=list(map(int,input().split()))
    a=[]
    b=[]
    for i in range(n):
        ai,bi=list(map(int,input().split()))
        a.append(ai)
        b.append(bi)
    return n,m,a,b

def main(n,m,a,b):
    jobList=[]
    for i in range(10**5+1):
        jobList.append([])
    for i in range(n):
        jobList[a[i]].append(b[i])

    goodjobs=[]
    earn=0
    for d in range(1,m+1):
        for job in jobList[d]:
            heappush(goodjobs,-job)
        #print(goodjobs)
        if len(goodjobs)>0:
            earn+=heappop(goodjobs)
    return -earn

def __starting_point():
    n,m,a,b=readinput()
    ans=main(n,m,a,b)
    print(ans)

__starting_point()
