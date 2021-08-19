import sys
my_file = sys.stdin
#my_file = open("1input.txt", "r")
n = int(my_file.readline())
a = [int(i) for i in my_file.readline().strip().split()]
a.sort()
b = list(range(1, n + 1))
# for i in range(n):
#     if a[i] <= n and a[i] >= 1:
#         b[i], b[a[i]-1] = b[a[i]-1], b[i]
turns = 0
for i in range(n):
    if a[i] < b[i]:
        turns += b[i] - a[i]
    elif a[i] > b[i]:
        turns += a[i] - b[i]
print(turns)
