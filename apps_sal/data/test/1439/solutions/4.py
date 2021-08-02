#import sys
#sys.stdin = open("python/in", "r")

#n = int(input().split(" "))
n, m = [int(i) for i in input().split(" ")]
arr = [int(i) % m for i in input().split(" ")]

c = {}
for i in range(m):
    c[i] = False

stack = [0]
newstack = []

for i in arr:
    for j in stack:
        arrrrgh = (i + j) % m
        if (arrrrgh == 0):
            print("YES")
            return
        elif (c[arrrrgh] == False):
            newstack.append(arrrrgh)
            c[arrrrgh] = True
    stack = stack + newstack
    newstack = []

print("NO")
