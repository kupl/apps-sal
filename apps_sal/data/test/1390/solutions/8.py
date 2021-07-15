import sys
my_file = sys.stdin
#my_file = open("input.txt", "r")
line = [int(i) for i in my_file.readline().strip('\n').split()]
n, m = line[0], line[1]
f = [int(i) for i in my_file.readline().split()]
f.sort()
min = f[n-1] - f[0]
for i in range(m):
    try:
        if f[n-1+i] - f[i] < min:
            min = f[n-1+i] - f[i]
    except:
        pass
print(min)
