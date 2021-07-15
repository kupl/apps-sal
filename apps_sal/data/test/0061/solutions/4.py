n, bx = map(int, input().split())
X = list(map(int, input().split()))
m, by = map(int, input().split())
Y = list(map(int, input().split()))
resX, resY = 0, 0
for i in range(n):
    resX += X[-i - 1] * bx ** i
for i in range(m):
    resY += Y[-i - 1] * by ** i
if(resX < resY):
    print("<")
elif(resX == resY):
    print("=")
else:
    print(">")
