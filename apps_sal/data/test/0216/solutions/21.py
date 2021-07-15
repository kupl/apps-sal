n = int(input())
a= list(map(int,input().split()))
for i in range(len(a)):
    a[i] = abs(a[i])
print(sum(a))
