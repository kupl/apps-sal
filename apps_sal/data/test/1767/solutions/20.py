n = int(input())
a = tuple(map(int, input().split()))
b = tuple(map(int, input().split()))

m = 0
def f(a,l,r):
    seq = a[l:r]
    ret = 0
    for i in seq:
        ret |= i
    return ret

# for leng in range(1, n+1):
#     for start in range(0, n-leng+1):
#         tmp = f(a, start, leng) + f(b, start, leng)
#         if tmp > m:
#             m = tmp
# print(tmp)
print(f(a, 0, len(a)) + f(b, 0, len(b)))

