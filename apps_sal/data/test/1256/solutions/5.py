import sys
f = sys.stdin
#f = open("input.txt", "r")
a = [int(i) for i in f.readline().split("+")]
a.sort()
for i in range(len(a)-1):
    print(a[i], end="+")
print(a[-1])
