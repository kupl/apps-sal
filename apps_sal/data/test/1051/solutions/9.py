n=int(input())
ip=list(map(int,input().split()))
if max(ip)>25:
    print(max(ip)-25)
else:
    print(0)

