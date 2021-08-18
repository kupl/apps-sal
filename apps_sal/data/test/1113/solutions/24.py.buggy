import sys

n = int(input())
l = list(map(int, input().split()))
pos_max = 0
for i in range(len(l)):
    if l[i] > pos_max:
        print(i + 1)
        return
    elif l[i] == pos_max:
        pos_max += 1
print("-1")
