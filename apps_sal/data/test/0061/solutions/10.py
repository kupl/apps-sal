(n, b) = list(map(int, input().split()))
x = list(map(int, input().split()))
(m, c) = list(map(int, input().split()))
y = list(map(int, input().split()))
x = x[::-1]
y = y[::-1]
X = 0
Y = 0
for i in range(len(x)):
    X += x[i] * b ** i
for i in range(len(y)):
    Y += y[i] * c ** i
if (X == Y):
    print("=")
elif (X < Y):
    print("<")
else:
    print(">")

