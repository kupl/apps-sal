import sys
n = int(input())
res = ''
arr = []
prsu = []
for i in range(2 * n - 2):
    s = input()
    arr.append(s)
    if len(s) == n - 1:
        prsu.append(s)
pos_pr = 0
pos_su = 0
for x in arr:
    if x == prsu[0][:len(x)]:
        pos_pr += 1
    if x == prsu[1][n - len(x):]:
        pos_su += 1
if pos_su >= n - 1 and pos_pr >= n - 1:
    prsu.reverse()
kek = [''] * len(arr)
ab_su = [0] * len(arr)
ab_pr = [0] * len(arr)
for i in range(len(arr)):
    if arr[i] == prsu[0][:len(arr[i])] and arr[i] != prsu[1][n - len(arr[i]) - 1:]:
        kek[i] = "P"
        ab_pr[len(arr[i]) - 1] = 1
    if arr[i] != prsu[0][:len(arr[i])] and arr[i] == prsu[1][n - len(arr[i]) - 1:]:
        kek[i] = 'S'
        ab_su[len(arr[i]) - 1] = 1
for i in range(len(arr)):
    if kek[i] == '':
        if not ab_pr[len(arr[i]) - 1]:
            kek[i] = 'P'
            ab_pr[len(arr[i]) - 1] = 1
        else:
            kek[i] = 'S'
            ab_su[len(arr[i]) - 1] = 1
right = True
for i in range(len(kek)):
    if kek[i] == 'P' and prsu[0][:len(arr[i])] != arr[i]:
        right = False
    if kek[i] == 'S' and arr[i] != prsu[1][n - len(arr[i]) - 1:]:
        right = False
if right:
    print(''.join(kek))
    return


prsu.reverse()
kek = [''] * len(arr)
ab_su = [0] * len(arr)
ab_pr = [0] * len(arr)
for i in range(len(arr)):
    if arr[i] == prsu[0][:len(arr[i])] and arr[i] != prsu[1][n - len(arr[i]) - 1:]:
        kek[i] = "P"
        ab_pr[len(arr[i]) - 1] = 1
    if arr[i] != prsu[0][:len(arr[i])] and arr[i] == prsu[1][n - len(arr[i]) - 1:]:
        kek[i] = 'S'
        ab_su[len(arr[i]) - 1] = 1
for i in range(len(arr)):
    if kek[i] == '':
        if not ab_pr[len(arr[i]) - 1]:
            kek[i] = 'P'
            ab_pr[len(arr[i]) - 1] = 1
        else:
            kek[i] = 'S'
            ab_su[len(arr[i]) - 1] = 1
print(''.join(kek))
