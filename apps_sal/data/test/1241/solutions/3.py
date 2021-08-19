# 1
# 0.1
# True
# "sdf"
#
# [1,2,True] : list
# (1,2,True) : tuple
# {1, 2, 3} : set
# {3: 2, True: False} : dict
# range(10) : range

# l = (1,2,True)
# print(l[0])
# l = 3
#
# s = {1, 2, True, "asdf", 2.1}
# print(s)
# d = {3: 2, True: False}
# print(d)
#
# if not (2 == 3 or 1 == 1.0):
#     print('2 = 3')
# elif True:
#     xxxxx
# else:
#     print('else')
#
# if 3 not in [1,2]:
#     print('2 not in 1,2')
#
# while True:
#     break
#     continue
# sdfadf

# while continue break

# for x in range(10):
#     if x % 11 == 12:
#         print(x)
#         break
# else:
#     print('nothing')

# l = []
# l.append(1)
# length = len(l)
# c = chr(96)
# print(c)

# l = ['a', 'b', 'c']
# print(l[2:3])

# s = {1, 2}
# s.add(3)
# r = {2,4,5,6}
# print(s | r)

# def f(x):
#     def mul(x, y):
#         return x * y
#     if x == 0:
#         return 1
#     else:
#         return mul(x, f(x-1))

# x = 1
# def f():
#     x = 1
# #     print(x)
# # f()
# # print(x)
#
# import os.path
# from os.path import join
#
# import numpy as np
# #import foo
# #
# class S:
#     def __init__(self, x):
#         self.x = x
#     def print_x(self):
#         self.y = 123
#         print(self.x)
#
# o = S(1)
# o.print_x()
# print(foo.x)
# print(np.array([1,2,3]))
#
# for x in ['1','2','3']:
#
#     print(join('/Users/kaoet', x, 'bar'))

# x = list(range(10))
# print(x)
# x = [i + 1 for i in x if i % 2 == 0]
# print(x)
# l = [ 1, 2,
#     1,
#     2,
# ]
#
# for x in range(10):
#     s = """
# asdfasdfas
# df
# sda
# f
# asdf
# as
# df
# asd
# f
# """
#
# print(s)


n, m = list(map(int, input().split()))

a = list(map(int, input().split()))

r = -1

ans = 0
ans_po = 0
for l in range(n):
    if l > 0:
        if a[l - 1] == 0:
            m += 1
    while (r < n - 1 and (1 - a[r + 1]) <= m):
        r += 1
        if (a[r] == 0):
            m = m - 1
            # print(m)

    if r - l + 1 > ans:
        ans = r - l + 1
        ans_po = l


print(ans)


for i in range(ans_po, ans_po + ans):
    a[i] = 1


print(' '.join(map(str, a)))
