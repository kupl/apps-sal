N = int(input())
U = 10**N
x1 = U - 9**N
x2 = U - 8**N
Y = 2 * x1 - x2
print(Y % (10**9 + 7))
