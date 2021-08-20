import sys
from statistics import median
from math import floor
sys.stdin.readline()
numbers = sorted((int(a) for a in sys.stdin.readline().split()))
print(numbers[floor((len(numbers) - 1) / 2)])
