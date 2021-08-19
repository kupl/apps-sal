import sys
my_file = sys.stdin
n = int(my_file.readline())
a = [int(i) for i in my_file.readline().strip().split()]
a.sort()
b = list(range(1, n + 1))
turns = 0
for i in range(n):
    if a[i] < b[i]:
        turns += b[i] - a[i]
    elif a[i] > b[i]:
        turns += a[i] - b[i]
print(turns)
