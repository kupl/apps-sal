l = int(input())
n = input().split()
for x in range(0, l):
    n[x] = int(n[x])
if l == 1 and (n[0] == 1):
    print("YES")
elif l-1 == sum(n) and l!=1:
    print("YES")
else:
    print("NO")
