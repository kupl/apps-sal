import sys
my_file = sys.stdin
#my_file = open("input.txt", "r")
line = my_file.readline().strip("\n").split()
n, k = int(line[0]), int(line[1])
a = my_file.readline().split()
count = 0
for i in a:
    if i.count("4") + i.count("7") <= k:
        count += 1
print(count)
