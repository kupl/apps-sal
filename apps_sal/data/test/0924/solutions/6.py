from collections import defaultdict
from fractions import gcd
def read_line():
    return [int(x) for x in input().split()]

la, ra, ta = read_line()
lb, rb, tb = read_line()


def check(la, ra, ta, lb, rb, tb):
  if la > lb:
      la, ra, ta, lb, rb, tb = lb, rb, tb, la, ra, ta

# print("{}--{}, {}--{}".format(la, ra, lb, rb))
    
  la, ra = 0, ra-la
  lb, rb = lb-la, rb-la

# print("{}--{}, {}--{}".format(la, ra, lb, rb))

def bf_solve(la, ra, ta, lb, rb, tb):
    ##p = ta*tb // gcd(ta, tb)
    A = [False for _ in range(tb)]
    for i in range(la, ra+1):
        A[i] = True
    A = A * (tb // gcd(ta, tb))
    
    B = [False for _ in range(tb)] 
    for i in range(lb, rb+1):
        B[i] = True
    B = B * (ta // gcd(ta, tb))
    # find longest common seq:
    streak = 0
    mx = 0
    A.append(False)
    B.append(False)
    for a, b in zip(A, B):
        if not(a and b):
            mx = max(mx, streak)
            streak = 0
        else:
            streak += 1
    return mx

def solve(la, ra, ta, lb, rb, tb):
    if la > lb:
        la, ra, ta, lb, rb, tb = lb, rb, tb, la, ra, ta

    # print("{}--{}, {}--{}".format(la, ra, lb, rb))

    old_la = la
    la, ra = 0, ra-old_la
    lb, rb = lb-old_la, rb-old_la
    # print("{}--{}, {}--{}".format(la, ra, lb, rb))
    # nonlocal la
    # nonlocal lb
    # nonlocal ra
    # nonlocal rb
    
    if gcd(ta, tb) == 1:
        return min(ra-la+1, rb-lb+1)
    d = gcd(ta, tb)
    dst = rb - lb
    lb = lb % d
    rb = lb + dst
    # print("{}--{}, {}--{}".format(la, ra, lb, rb))

    both_start = max(la, lb)
    both_end = min(ra, rb)
    # print("common {}--{}".format(both_start, both_end))
    res_cand = max(both_end - both_start + 1, 0)

    lb -= d
    rb -= d
    assert lb < 0
    both_start = max(la, lb)
    both_end = min(ra, rb)
    # print("{} __ {}, {} __ {}".format(la, ra, lb, rb))
    # print("common {} __ {}".format(both_start, both_end))
    res_cand2 = max(both_end - both_start + 1, 0)
    return max(res_cand, res_cand2)

print(solve(la, ra, ta, lb, rb, tb))
# return
    
# print(solve())


def check(la, ra, ta, lb, rb, tb):
  A = solve(la, ra, ta, lb, rb, tb)
  B = bf_solve(la, ra, ta, lb, rb, tb)

  assert A == B, (A, B)

# for ta in range(2, 10):
#     for tb in range(2, 10):
#         for la in range(ta):
#             for ra in range(la, ta):
#                 for lb in range(tb):
#                     for rb in range(lb, tb):
#                         print(la, ra, ta, lb, rb, tb)
#                         check(la, ra, ta, lb, rb, tb)
    

