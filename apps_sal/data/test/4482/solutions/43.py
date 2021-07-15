N=int(input())
a=list(map(int,input().split()))

A=sum(a)//N
B=(sum(a)-1)//N+1


print((min(sum((x-A)*(x-A) for x in a),sum((x-B)*(x-B) for x in a))))

