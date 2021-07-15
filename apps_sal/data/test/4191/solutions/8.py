def myor(a, b):
    return a | b

def myxor(a, b):
    return a ^ b

def myand(a, b):
    return a & b


op1 = myxor
op2 = myor
op3 = myand

l = [int(input()) for _ in range(4)]

print(op1(op3(op1(l[0], l[1]), op2(l[2], l[3])), op2(op3(l[1], l[2]), op1(l[0], l[3]))))
