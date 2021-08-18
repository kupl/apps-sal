import sys
import math
import re

sys.setrecursionlimit(10 ** 8)
def ini(): return int(sys.stdin.readline())
def inm(): return map(int, sys.stdin.readline().split())
def inl(): return list(inm())
def ins(): return sys.stdin.readline().rstrip()


debug = lambda *a, **kw: print("\033[33m", *a, "\033[0m", **dict(file=sys.stderr, **kw))

s2 = input()
t = input()

s2_r = s2[::-1]
t_r = t[::-1]

ans_flag = False
for i in range(len(s2)):
    for j in range(i + 1, len(s2) + 1):
        if (j - i) == len(t_r):
            flag = True
            for k, l in enumerate(range(i, j)):
                if s2_r[l] != t_r[k] and s2_r[l] != '?':
                    flag = False
            if flag == True:
                ans = s2_r[:i] + t_r + s2_r[j:]
                ans = ans.replace('?', 'a')
                ans = ans[::-1]
                print(ans)
                ans_flag = True
                break

    else:
        continue
    break

if ans_flag == False:
    print('UNRESTORABLE')
