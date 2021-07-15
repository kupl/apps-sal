n = int(input())
a = list(map(int,input().split()))
l = [0] * n
for i in range(n):
    l[a[i]-1] = i + 1
print(*l)
