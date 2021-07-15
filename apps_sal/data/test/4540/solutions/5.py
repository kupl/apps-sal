n = int(input())
arr = [0] + list(map(int, input().split())) + [0]
sum_arr = sum(abs(arr[i] - arr[i+1]) for i in range(n+1))

for i in range(1, n+1):
    diff = abs(arr[i-1] - arr[i]) + abs(arr[i] - arr[i+1])\
               - abs(arr[i-1] - arr[i+1])
    print(sum_arr - diff)
