import sys

input = sys.stdin.readline

n = int(input())
h_list = list(map(int, input().split()))

tmp = 0
flag = False

for h in h_list:

    if tmp == 0:
        tmp = h
        continue

    if tmp > h:
        if tmp - 2 >= h:
            print("No")
            return
        tmp = h
        if flag:
            print("No")
            return
        else:
            flag = True
    elif tmp < h:
        tmp = h
        flag = False

print("Yes")

