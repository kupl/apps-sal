import sys
n = input()
cand = [str(i) + str(i) + str(i) for i in range(10)]
for ci in cand:
    if n.count(ci) >= 1:
        print("Yes")
        return
print("No")
