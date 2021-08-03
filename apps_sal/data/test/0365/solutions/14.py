n, x = list(map(int, input().split()))
a = list(map(int, input().split()))
s = 0
for i in a:
    s += i
if (s == x - n + 1) or (n == 0):
    print("YES")
else:
    print("NO")
