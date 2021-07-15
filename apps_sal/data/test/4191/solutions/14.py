a = int(input())
b = int(input())
c = int(input())
d = int(input())
def f(a, b, c, d):
    #return ((a & b) ^ (c | d)) & ((b ^ c) | (a & d))
    return ((a ^ b) & (c | d)) ^ ((b & c) | (a ^ d))
    #return ((a | b) & (c ^ d)) | ((b & c) ^ (a | d))
print(f(a, b, c, d))
