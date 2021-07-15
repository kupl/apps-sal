import sys
s = []

for i in range(int(input())):
    W = input()
    if W in s:
        print("No")
        return
    if len(s) != 0 and s[-1][-1] != W[0]:
        print("No")
        return
    s.append(W)
print("Yes")
