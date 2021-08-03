a1, b1 = list(map(int, input().split()))
a2, b2 = list(map(int, input().split()))
a3, b3 = list(map(int, input().split()))
print(3)
a4 = a1 + a2 - a3
b4 = b1 + b2 - b3
print(a4, b4)
a4 = a1 + a3 - a2
b4 = b1 + b3 - b2
print(a4, b4)
a4 = a3 + a2 - a1
b4 = b3 + b2 - b1
print(a4, b4)
