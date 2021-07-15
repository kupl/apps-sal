
# A
# print(int(input()) % 2)

# B
# good = ['cool', 'great', 'not bad']
# for i in range(10):
#     print(i, flush=True)
#     r = input().strip().lower()
#     for g in good:
#         if g in r:
#             print('normal')
#             return
# print('grumpy')

# C
# input()
# a = [int(x) for x in input().split()]
# while a:
#     for i in range(len(a)-1):
#         if abs(a[i] - a[i+1]) >= 2:
#             print('NO')
#             return
#     a.pop(a.index(max(a)))
# print('YES')

# D
# print(20)

# E
n = int(input())
a, b = 0, 0
for _ in range(n):
    _, s = input().split()
    if s == 'soft':
        a += 1
    else:
        b += 1
if a < b:
    a, b = b, a
x = 0
for i in range(1, 200):
    x += 1 + (i*2 - 1) // 4 * 2
    if a <= x and b <= i**2 - x:
        print(i)
        break

# G
# s = [ord(x) in input().strip()]

