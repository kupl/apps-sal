n = int(input())
w = list(map(int,input().split()))
s = sum(w)
a = b = 0
ans = s
for i in range(n):
    a+=w[i]
    b = s-a
    if abs(a-b)<ans:
        ans = abs(a-b)
print(ans)
