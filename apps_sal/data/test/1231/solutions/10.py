
import sys, math

a, b = [int(x) for x in sys.stdin.readline().split()]

print('YES' if (a > 0 or b > 0) and math.fabs(a-b) <= 1 else 'NO')

