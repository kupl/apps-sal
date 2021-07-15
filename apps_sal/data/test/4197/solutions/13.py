n=int(input())
a=list(map(int,input().split()))
ans = []
for i in range(n):
    ans.append(0)
for i in range(n):
    ans[a[i]-1] = i +1
for i in range(len(ans)):
    print(ans[i], end=" ")
