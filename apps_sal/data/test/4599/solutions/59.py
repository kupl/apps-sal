n = int(input())
a = list(map(int,input().split()))
a.sort(reverse=True)
al = 0
bo = 0
for i in range(n):
    if i%2==0:
        al += a[i]
    else:
        bo += a[i]
print(al-bo)
