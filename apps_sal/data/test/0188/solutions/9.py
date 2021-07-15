import sys
n, k = [ int(x) for x in input().split() ]
arr = list( map( int, input().split()) )

cnt_2 = 2 * n
cnt_4 = n
cnt_1 = 0

i = 0
while(cnt_4 > 0 and i < k):
    tmp = int(arr[i] / 4)
    if(tmp > 0 and cnt_4 > 0):
        arr[i] = arr[i] - 4 * min(tmp, cnt_4)
        cnt_4 = cnt_4 - min(tmp, cnt_4)
    i = i + 1

if(cnt_4 > 0):
    cnt_2 = cnt_2 + cnt_4
    cnt_1 = cnt_1 + cnt_4
    cnt_4 = 0

i = 0
while(cnt_2 > 0 and i < k):
    tmp = int(arr[i] / 2)
    if(tmp > 0 and cnt_2 > 0):
        arr[i] = arr[i] - 2 * min(tmp, cnt_2)
        cnt_2 = cnt_2 - min(tmp, cnt_2)
    i = i + 1

if(cnt_2 > 0):
    cnt_1 = cnt_1 + cnt_2
    cnt_2 = 0

i = 0
while(i < k):
    tmp = arr[i]
    if(tmp > cnt_1):
        print("NO")
        return
    elif(tmp > 0 and tmp <= cnt_1):
        cnt_1 = cnt_1 - tmp
        arr[i] = arr[i] - tmp
    i = i + 1

print("YES")

