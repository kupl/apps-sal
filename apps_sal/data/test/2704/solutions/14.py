n, q = list(map(int, input().split()))
l = list(map(int, input().split()))
a = max(l)
b = min(l)
for i in range(q):
    y = int(input())
    if y >= b and y <= a:
        print("Yes")
    else:
        print("No")
