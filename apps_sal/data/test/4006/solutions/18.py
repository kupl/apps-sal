"""
@Project : CodeForces
@File    : 1.py 
@Time    : 2019/4/26 22:31
@Author  : Koushiro 
"""


def find(num):
    num += 1
    while num % 10 == 0:
        num = num // 10
    return num


def __starting_point():
    n = int(input())
    dic = {n: 1}
    n = find(n)
    while n not in dic:
        dic[n] = 1
        n = find(n)
    print(len(dic))


__starting_point()
