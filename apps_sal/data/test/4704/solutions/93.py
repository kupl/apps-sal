n = int(input())
a = list(map(int,input().split()))
li = [a[0]]
for i in range(n-1):
    li.append(li[i]+a[i+1])

b = []
for i in range(n-1):
    b.append(abs(li[-1]-li[i]*2))
print(min(b))
