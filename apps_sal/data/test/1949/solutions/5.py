n, k = list(map(int, input().split(' ')))

arr = list(map(int, input().split(' ')))

arr.sort()

i = 0
s = 0

while(k > 0):
    while(i < n and arr[i] <= s):
        i += 1

    if(i >= n):
        print(0)
    else:
        print(arr[i] - s)
        s += (arr[i] - s)

    k -= 1
