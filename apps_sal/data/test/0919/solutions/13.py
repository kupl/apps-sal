n, k = input().strip().split(' ')
n, k = int(n), int(k)
s = input()
arr = []
for i in s:
    arr.append(i)
arr.sort()
# print(arr)
wt = 0
prev = -2
for i in arr:
    if(prev + 2 <= ord(i) - 96):
        wt += ord(i) - 96
        prev = ord(i) - 96
        k -= 1
    if(not k):
        break
if(k):
    print(-1)
else:
    print(wt)
