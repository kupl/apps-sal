n = int(input())

L = list(map(int, input().split()))
L.sort(reverse=True)
x = 0
y = 0

for i in range(n):
    if(x < y):
        x += L[i]
    else:
        y += L[i]
if(x == y):
    print("YES")
else:
    print("NO")
