a = int(input())
b = int(input())
c = int(input())
apb = a + b
bpc = b + c
ab = a * b
bs = b * c
apbpc = a + b + c
abc = a * b * c
print(max(apb * c, bpc * a, ab + c, bs + a, apbpc, abc))
