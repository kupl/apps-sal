import sys
my_file = sys.stdin
#my_file = open("input.txt", "r")
num = [int(i) for i in my_file.readline().strip("\n").split(" ")]
n = num[0]
k = num[1]
rest = []
max = -1000000000
for i in my_file.readlines():
    rest = [int(k) for k in i.strip("\n").split(" ")]
    if rest[0] > max:
        if rest[1] <= k:
            max = rest[0]
        elif rest[0] - (rest[1] - k) > max:
            max = rest[0] - (rest[1] - k)
print(max)
