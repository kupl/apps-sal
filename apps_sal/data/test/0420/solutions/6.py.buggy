n, m = map(int, input().split())

ans = n

arr = []
for i in range(n):
    arr.append(input())

while True:
    if n & 1:
        print(ans)
        break
    else:
        k = n // 2
        for i in range(k):
            if arr[i] != arr[n - i - 1]:
                print(ans)
                return
        n = k
        ans = n
