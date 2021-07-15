n, x = [int(i) for i in input().split()]

a = [int(i) for i in input().split()]

if sum(a) == (x - n + 1):
    print("YES")
else:
    print("NO")
