n = int(input())
a = [0] + list(map(int,input().split()))
l = [0]*n
for i in a:
    l[i-1] += i
for j in range(n):
    l[j] = int(l[j]/(j+1))
for k in l:
    print(k,end="\n")
