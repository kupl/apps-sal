# self.author = Fuad Ashraful Mehmet ,CSE-UAP

from sys import stdin
input=stdin.readline


def fun():
    n=int(input())
    ans=n*(n**2+3*n+2)//6

    for _ in range(n-1):
        a,b=map(int,input().split())

        if a>b:
            a,b=b,a
        ans-=a*(n-b+1)
    print(ans)

fun()
