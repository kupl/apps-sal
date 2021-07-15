3
import sys

n = int(sys.stdin.readline())
a = [int(x) for x in sys.stdin.readline().split()]

def is_valid(s, k):
    # Ali lahko zapakiramo s steklenic v škatle velikosti k in k + 1?
    # s = x * k + y * (k + 1) = (x + y) * k + y, kjer je 0 <= y < k
    y = s % k
    return s // k >= y

def all_valid(a, k):
    for s in a:
        if not is_valid(s, k):
            return False
    return True

best_sol = 1

k = 1
while k*k <= a[0]:
    if all_valid(a, k):
        best_sol = max(best_sol, k)
    k += 1

# t je skupno število škatel.
t = 1
while t*t <= a[0]:
    k = a[0] // t
    if all_valid(a, k):
        best_sol = max(best_sol, k)
    if a[0] % t == 0 and k > 1:
        if all_valid(a, k - 1):
            best_sol = max(best_sol, k - 1)
    t += 1

# print(best_sol, best_sol + 1)

print(sum(s // (best_sol + 1) + (0 if s % (best_sol + 1) == 0 else 1) for s in a))

