from sys import stdin
import heapq
def main():
    #入力
    readline=stdin.readline
    x,y,z,k=map(int,readline().split())
    a=list(map(int,readline().split()))
    a.sort(reverse=True)
    b=list(map(int,readline().split()))
    b.sort(reverse=True)
    c=list(map(int,readline().split()))
    c.sort(reverse=True)

    s={(0,0,0)}
    h=[[-(a[0]+b[0]+c[0]),(0,0,0)]]
    heapq.heapify(h)
    for _ in range(k):
        li=heapq.heappop(h)
        n=-li[0]
        co=li[1]
        print(n)

        if co[0]+1<x:
            co_1=(co[0]+1,co[1],co[2])
            n_1=a[co_1[0]]+b[co_1[1]]+c[co_1[2]]
            n_1=-n_1
            if co_1 not in s:
                heapq.heappush(h,[n_1,co_1])
                s.add(co_1)

        if co[1]+1<y:
            co_2=(co[0],co[1]+1,co[2])
            n_2=a[co_2[0]]+b[co_2[1]]+c[co_2[2]]
            n_2=-n_2
            if co_2 not in s:
                heapq.heappush(h,[n_2,co_2])
                s.add(co_2)

        if co[2]+1<z:
            co_3=(co[0],co[1],co[2]+1)
            n_3=a[co_3[0]]+b[co_3[1]]+c[co_3[2]]
            n_3=-n_3
            if co_3 not in s:
                heapq.heappush(h,[n_3,co_3])
                s.add(co_3)

def __starting_point():
    main()
__starting_point()
