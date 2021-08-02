W, H, X, Y = map(int, input().split())

a = W * H // 2
if W * H % 2 == 1:
    a = str(a) + ".5"
b = int(W == X * 2 and H == Y * 2)
print(a, b)
