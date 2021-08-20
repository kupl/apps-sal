(r, D, a_2000) = input().split()
r = int(r)
D = int(D)
a_2000 = int(a_2000)
b = D / (r - 1)
for i in range(1, 11):
    print(int(r ** i * (a_2000 - b) + b))
