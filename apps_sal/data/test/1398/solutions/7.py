import bisect
import sys
sys.stdin = open('input.txt', 'r')
sys.stdout = open('output.txt', 'w')


def find_ge(a, x):
    i = bisect.bisect_left(a, x)
    if i != len(a):
        return i


n = int(input())
array = sorted([int(i) for i in input().split()])
double = [2 * i for i in array]
minimum = n
for i in range(n - 1, -1, -1):
    minimum = min(n - 1 - i + find_ge(double, array[i]), minimum)
print(minimum)
