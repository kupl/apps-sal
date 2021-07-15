
a, b = map(int, input().split())

a_b = str(a) * b
b_a = str(b) * a

if int(a_b[0]) >= int(b_a[0]):
    print(b_a)
else:
    print(a_b)
