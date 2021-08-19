n = int(input().split()[0])
a = input().split()
b = input().split()
a_bit = 0
b_bit = 0
for i in range(n):
    a_bit |= int(a[i])
    b_bit |= int(b[i])
print(a_bit + b_bit)
