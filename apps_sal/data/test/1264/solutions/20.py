import sys
my_file = sys.stdin
#my_file = open("input.txt", "r")
n = int(my_file.readline().strip())
a = [int(i) for i in my_file.readline().strip().split()]
max = 0
for end in range(n, -1, -1):
    for begin in range(end):
        s = sum(a[:begin] + [i ^ 1 for i in a[begin:end + 1]] + a[end:])
        if s > max:
            max = s
print(max)
