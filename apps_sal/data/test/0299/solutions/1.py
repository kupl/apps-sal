import sys
my_file = sys.stdin
#my_file = open("input.txt", "r")
n = int(my_file.readline().strip("\n"))
a = [int(i) for i in my_file.readline().split()]
if sum(a[::3]) >= sum(a[1::3]) and sum(a[::3]) >= sum(a[2::3]):
    print("chest")
elif sum(a[1::3]) >= sum(a[::3]) and sum(a[1::3]) >= sum(a[2::3]):
    print("biceps")
else:
    print("back")
