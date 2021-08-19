import math

# input
n, k = map(int, input().split())
flist = [int(x) for x in input().split()]


# variables
time = 0


# main
flist.sort()
flist.reverse()
if n <= k:
    print(2 * flist[0] - 2)
    quit()

for i in range(math.ceil(n / k)):
    time += 2 * flist[k * i] - 2

print(time)
