inp = input().split(" ")
k = 0
l = []
a = int(inp[0])
n = ((-1)**a) * a
if n % 2 == 0:
    k = n / 2
else:
    k = (n // 2)
print(int(k))
