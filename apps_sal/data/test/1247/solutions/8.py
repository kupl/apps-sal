# import sys
# f = sys.stdin
# f = open("input.txt", "r")
a = input()
b = dict()
for i in set(a):
    if a.count(i) % 2 != 0:
        b[i] = a.count(i)
if len(b) > 1:
    if (len(b) - 1) % 2:
        print("Second")
    else:
        print("First")
else:
    print("First")
