n = int(input())
f = False
for i in range(n):
    q, w, e = input().split()
    if (int(w) >= 2400 and int(e) > int(w)):
        f = True
if f:
    print("YES")
else:
    print("NO")
