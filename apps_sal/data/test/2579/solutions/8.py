from bisect import bisect

l,r,x,y,k = [int(x) for x in input().strip().split()]

least = l/y
most = r/x


if (k < least or k > most):
    print("NO")
    return

for i in range(x,y+1):
    if k*i == l + max(0,bisect(range(l, r+1), k*i) - 1):
        print("YES")
        return

print("NO")
