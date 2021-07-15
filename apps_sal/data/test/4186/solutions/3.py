n = int(input())
a = [int(x) for x in input().split()]
a = sorted(a)
#print(a)
c = 0
for i in range(1,n,2):
    c = c + a[i] - a[i-1]
print(c)
