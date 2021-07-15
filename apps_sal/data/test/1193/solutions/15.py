b=input().split()
n=int(b[0])
k=int(b[1])
a=input().split()
ai=[]
for i in range(n):
    ai.append(int(a[i]))
ai.sort()
print(ai[n-k])

