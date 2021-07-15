import sys
n = input()
a = [int(x) for x in input().split()]
ac = list(a)
r = []
ok = True

for i in range(len(a) - 1):
    if (abs(a[i] - a[i + 1]) >= 2):
        print ("NO")
        return
a = list(sorted(a))

for i in range(len(a) - 1):
    if (abs(a[i] - a[i + 1]) >= 2):
        print ("NO")
        return
        
print ("YES")
