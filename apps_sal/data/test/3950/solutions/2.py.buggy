import sys
n, q = map(int, input().split())
a = list(map(int, input().split()))
l = len(a)

zeros = []
last = dict()
cur_max = 0
last_max = 1

stack = []

for i in range(l - 1, -1, -1):
    if a[i] == 0:
        zeros.append(i)
    elif a[i] not in last:
        last[a[i]] = i
for i in range(l):

    if a[i] == 0:
        a[i] = max(cur_max, 1)
    elif a[i] > cur_max and last[a[i]] != i:
        stack.append(cur_max)
        cur_max = a[i]
    elif cur_max != 0 and i == last[cur_max]:
        cur_max = stack.pop()
    elif a[i] < cur_max:
        print("NO")
        return

if q > max(a):
    if zeros:
        print("YES")
        a[zeros[0]] = q
        print(*a)
    else:
        print("NO")
elif q == max(a):
    print("YES")
    print(*a)
elif q < max(a):
    print("NO")
