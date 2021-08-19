import sys
# from collections import deque
input = sys.stdin.readline


def binary_search(org, arr, l, r, n, L, value):
    mid = (l + r) // 2
    # print(mid,"ppppp")
    if(mid > 0 and arr[mid] - value >= org and arr[mid - 1] - value < org):
        return mid
    elif(mid == 0 and arr[mid] - value >= org):
        return mid
    elif(mid == L and arr[mid] - value >= org):
        return mid

    elif(mid == n):
        return mid

    elif(mid > 0 and arr[mid] - value > org and arr[mid - 1] - value >= org):
        return binary_search(org, arr, l, mid, n, L, value)

    elif(arr[mid] - value < org):
        # print("dddddd")
        return binary_search(org, arr, mid + 1, r, n, L, value)
    return mid


n = int(input())
l = list(map(int, input().split()))
u = list(map(int, input().split()))
extra = [0] * n
pre = [0] * n
t = [0] * n
t[0] = u[0]
for i in range(1, n):
    t[i] += t[i - 1] + u[i]
# print(t)
for i in range(n):
    if(i > 0):
        v = t[i - 1]
    else:
        v = 0
    index = binary_search(l[i], t, i, n - 1, n - 1, i, v)
    # print(i,index)
    if(index > 0 and index != i):
        value = t[index] - t[index - 1]
        remain = l[i] - (t[index - 1] - v)
    elif(index > 0 and index == i):
        value = t[index] - t[index - 1]
        remain = l[i]

    else:
        value = t[index]
        remain = l[i]
    if(value >= remain):
        extra[index] += remain
        # print(extra[index],"ooooo")
    elif(remain > value):

        extra[index] += value
        # print(extra[index],"oooooopp")
    if(i > 0 and index > 0):
        pre[i - 1] -= 1
        pre[index - 1] += 1
    elif(i == 0 and index > 0):
        pre[index - 1] += 1
    elif(i == 0 and index == 0):
        continue
    # print(extra,pre)
# print(extra,pre)
for i in range(n - 2, -1, -1):
    pre[i] += pre[i + 1]
# print(extra,pre)
r = [0] * n
for i in range(n):
    r[i] = (u[i] * pre[i]) + extra[i]

for i in r:
    print(i, end=" ")
