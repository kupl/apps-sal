import math


def average(args):
    sum = 0
    count = 0
    for arg in args:
        sum += arg
        count += 1
    if count > 0:
        sum = sum / count
    return sum


n = int(input())
args = [int(x) for x in input().split()]
avg = average(args)
up = 0
down = 0
for arg in args:
    if arg > avg:
        down += arg - math.ceil(avg)
    elif arg < avg:
        up += math.floor(avg) - arg
print(max(up, down))
