import sys
import math

# to read string


def get_string(): return sys.stdin.readline().strip()
# to read list of integers
def get_int_list(): return list(map(int, sys.stdin.readline().strip().split()))
# to read integers
def get_int(): return int(sys.stdin.readline())
# to print fast
def pt(x): return sys.stdout.write(str(x) + '\n')


#--------------------------------WhiteHat010--------------------------------------#
n = get_int()
prev_t, s = get_int_list()
mx_q = s
q_size = s

for i in range(n - 1):
    t, s = get_int_list()
    diff = t - prev_t
    q_size = max(0, q_size - diff)
    q_size = q_size + s
    mx_q = max(mx_q, q_size)
    prev_t = t
print(prev_t + q_size, mx_q)
