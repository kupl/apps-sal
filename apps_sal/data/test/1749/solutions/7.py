n, l, r = map(int, input().split())
l -= 1
r -= 1
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for i in range(n):
    if (b[i] != a[i]) and (i < l or i > r):
        print("LIE")
        break
else:
    print("TRUTH")
