import sys
l = int(sys.stdin.readline())
n = list(sys.stdin.readline())
a = [0] * 26
for i in n[:-1]:
    j = ord(i)
    if j > 91:
        j = j - 32
    j = j - 65
    a[j] = 1
    if sum(a) == 26:
        print("YES")
        break
if sum(a) != 26:
    print("NO")
