from sys import stdin, stdout

l, r, x, y, k = list(map(int, stdin.readline().rstrip().split()))

if k * x > r or k * y < l:
    print("NO")
elif int(r / k) == int(l / k) and int(l / k) != l / k:
    print("NO")
else:
    print("YES")
