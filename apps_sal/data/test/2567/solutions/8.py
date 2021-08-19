import sys
sys.setrecursionlimit(10000)
# default is 1000 in python

# increase stack size as well (for hackerrank)
# import resource
# resource.setrlimit(resource.RLIMIT_STACK, (resource.RLIM_INFINITY, resource.RLIM_INFINITY))


t = int(input())
# t = 1

for _ in range(t):
    n = int(input())
    s = input()
    ans = ""
    for i in range(n):
        ans += s[n - 1]
    print(ans)


# try:
    # raise Exception
# except:
    # print("-1")


# from itertools import combinations
# all_combs = list(combinations(range(N), r))


# from collections import OrderedDict
# mydict = OrderedDict()


# thenos.sort(key=lambda x: x[2], reverse=True)


# int(math.log(max(numbers)+1,2))


# 2**3 (power)


# a,t = (list(x) for x in zip(*sorted(zip(a, t))))


# to copy lists use .copy()


# pow(p, si, 1000000007) for modular exponentiation


# my_dict.pop('key', None)
# This will return my_dict[key] if key exists in the dictionary, and None otherwise.


# bin(int('010101', 2))
