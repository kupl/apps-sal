input_str = input()
n, x = int(input_str.split()[0]), int(input_str.split()[1])
input_str = input()
a = input_str.split()
s = 0
for i in range(n):
    a[i] = int(a[i])
    # a.append(1000000000)
    s += a[i]

'''
a = []
for i in range(n):
    if i<65536:
        temp = 1
    else:
        temp = 0#random.randint(0, 1000000000)
    s += temp
    a.append(temp)#(557523474, 999999999))'''

sum_a = [s - a[i] for i in range(n)]
minimum = min(sum_a)
res = pow(x, minimum, 1000000007)  # FastPow(x, minimum)#x**minimum
sum_xa = 0
s_new = s - minimum
for i in range(n):
    sum_xa += pow(x, s_new - a[i], 1000000007)  # FastPow(x, s_new - a[i])

deg = 0
deg_zn = s - minimum
ts = sum_xa
while sum_xa % 1 == 0 and deg_zn:
    sum_xa /= x
    deg += 1
    deg_zn -= 1
  #  print (deg, sum_xa%1==0)
# if (n, x) == (98304, 2):
#    print (minimum, s, ts, deg)


if deg:
    res *= pow(x, deg - 1 if sum_xa % 1 != 0 else deg)
print(res % 1000000007)
