A, B = list(map(int, input().split()))
# a = A
# if A == B:
#     print(A)
#     return
# if A != 0:
#     a = A - 1
# if a % 2 != 0:
#     a = a ^ (a - 1)
#     t = (a - 1) // 2
#     if t % 2 != 0:
#         a = a ^ 1
# else:
#     t = A // 2
#     if t % 2 != 0:
#         a = a ^ 1
#
# if B % 2 != 0:
#     B = B ^ (B - 1)
#     t = (B - 1) // 2
#     if t % 2 != 0:
#         B = B ^ 1
# else:
#     t = B // 2
#     if t % 2 != 0:
#         B = B ^ 1
# ans = a ^ B


def calc(a):
    t = (a + 1) // 2
    ans = t % 2
    if a % 2 == 0:
        ans = ans ^ a
    return ans


print((calc(A - 1) ^ calc(B)))
