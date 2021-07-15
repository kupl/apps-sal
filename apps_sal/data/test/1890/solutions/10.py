input_string = input()
n = int(input())
len_tmp = len(input_string)
const = 1000000007

def fast_pow(a, b, mod):
    c=bin(b)[2:]
    result=1
    for i in c:
        result = (result*result * a**int(i))%mod
    return result

def inverse(a, mod):
    #mod-простое
    return fast_pow(a, mod-2, mod)
#-------------------------------
num = 0
tmp = 1
"""
for i in range(len_tmp):
    if int(input_string[i])%5==0:
        num = (num + fast_pow(2, i, const))
"""
for i in range(len_tmp):
    if int(input_string[i])%5==0:
        num = (num + tmp)
    tmp=(tmp*2)%const
num %= const
l = fast_pow(2, len_tmp, const)
print((num*(fast_pow(l, n, const)-1)*inverse(l-1, const))%const)
