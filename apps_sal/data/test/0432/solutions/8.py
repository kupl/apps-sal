def main():
        n=int(input())
        c=[int(i) for i in input().split()]
        a=[int(i) for i in input().split()]
        vis=[0]*(n+1)
        sum=0
        for i in range(1,n+1):
                x=i
                while(vis[x]==0):
                        vis[x]=i
                        x=a[x-1]
                if vis[x]!=i:
                        continue
                p=x
                cos=c[x-1]
                while(p!=a[x-1]):
                        x=a[x-1]
                        cos=min(c[x-1],cos)
                sum=sum+cos
        return sum
print(main())

