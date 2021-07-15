n = int(input())
a = sorted(list(map(int,input().split())))
m = int(input())
q = list(map(int,input().split()))
s = sum(a)
for i in range(m):
    print(s - a[n - q[i]])
