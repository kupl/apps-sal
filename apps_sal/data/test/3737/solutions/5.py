n = int(input())
s = [int(i) for i in input().split()]
a = max(s)
b = min(s)
ans = 0
for i in s:
    if i!= a and i!=b:
        ans+=1
print(ans)
