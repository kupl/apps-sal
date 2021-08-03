n, x = [int(i) for i in input().split()]
a = [int(j) for j in input().split()]
s = sum(a)
if s + n - 1 == x:
    print("YES")
else:
    print("NO")
