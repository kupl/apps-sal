n = int(input())
arr = list(map(int, input().strip().split(' ')))
arr.sort()
s = sum(arr)
if(s >= 4.5 * n):
    print(0)
else:
    cnt = 0
    for i in range(n):
        cnt += 1
        s = s - arr[i] + 5
        if(s >= 4.5 * n):
            break
    print(cnt)
