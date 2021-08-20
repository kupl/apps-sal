n = int(input())
arr = input().split('W')
for i in range(arr.count('')):
    arr.remove('')
print(len(arr))
if len(arr):
    s = ''
    for x in arr:
        s += str(len(x)) + ' '
    print(s)
