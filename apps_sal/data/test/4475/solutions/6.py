#Bhargey Mehta (Senior)
#DA-IICT, Gandhinagar
import sys, math
mod = 10**9 + 7

def goSolve(a, b, x, y, n):
    d = min(n, a-x)
    a -= d
    n -= d
    d = min(n, b-y)
    b -= d
    return a * b

def solve(test_index):
    a, b, x, y, n = list(map(int, input().split()))
    print(min(goSolve(a, b, x, y, n), goSolve(b, a, y, x, n)))
    return

if 'PyPy' not in sys.version:
    sys.stdin = open('input.txt', 'r')

sys.setrecursionlimit(100000)
num_tests = 1
num_tests = int(input())
for test in range(1, num_tests+1):
    #print("Case #{}: ".format(test), end="")
    solve(test)

