import sys
import io

stream_enable = 0

inpstream = """
9 5
"""

if stream_enable:
    sys.stdin = io.StringIO(inpstream)
    input()


def inpmap():
    return list(map(int, input().split()))


a, b = inpmap()
if b > a:
    print(0)
    return
flag = a == b
# a = bin(a)[2:]
# b = bin(b)[2:]
# ln = max(len(a), len(b))
# if len(a) > len(b):
#     b = "0" * (len(a) - len(b)) + b
# elif len(b) > len(a):
#     a = "0" * (len(b) - len(a)) + a
# ln = len(a)
# print(a)
# print(b)
b = "0" * (len(bin(a)) - len(bin(b))) + bin(b)[2:]
# print(b)
res = 1
p = 2 ** (len(b) - 1)
for x in b:
    if x == '1':
        res *= 2
        a -= p
    elif a >= p * 4 - 1:
        print(0)
        return
    elif a >= p * 2:
        a -= p * 2
    p //= 2
    # print(a)
if a:
    print(0)
    return
if flag:
    res -= 2
print(res)
