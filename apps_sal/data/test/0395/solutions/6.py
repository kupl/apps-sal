arr = list(map(int, input().split()))
n = 6
sm = sum(arr)
for i in range(n):
    for i1 in range(i):
        for i2 in range(i1):
            if sm - arr[i] - arr[i1] - arr[i2] == arr[i] + arr[i1] + arr[i2]:
                print("YES")
                return
print("NO")
