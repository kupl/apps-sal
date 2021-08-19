"""
arr = list(map(int, input().split()))
n,k=map(int, input().split())
"""
import math
import sys
# input = sys.stdin.readline

############ ---- Input Functions ---- ############


def inp():
    return(int(input()))


def inlt():
    return(list(map(int, input().split())))


def insr():
    s = input()
    return(list(s[:len(s) - 1]))


def invr():
    return(list(map(int, input().split())))


test_cases = int(input())
for _ in range(test_cases):
    sides = int(input())
    sides *= 2
    apothem = 1 / (2 * math.tan((180 / sides) * (math.pi / 180)))
    print(2 * apothem)
# for _ in range(test_cases):
#     size = int(input())
#     arr = inlt()
#     maxx = -float('inf')
#     temp = []
#     max_diff = 0
#     #Checks the maximum number and difference of decreasing numbers, the moment it increases again, it rechecks for a bigger difference
#     for i in range(size):
#         if arr[i] < maxx:
#             max_diff = max(max_diff, maxx - arr[i])
#         maxx = max(arr[i], maxx)
#     i = 0
#     index = 0
#     while i < max_diff:
#         i += 2 ** index
#         index += 1
#     print(index)
