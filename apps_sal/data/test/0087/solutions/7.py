from sys import stdin
import math

days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

M, D = list(map(int, stdin.readline().split()))
M -= 1
D -= 1

print(math.ceil((days_in_month[M] + D) / 7))
