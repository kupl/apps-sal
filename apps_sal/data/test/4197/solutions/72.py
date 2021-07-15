n = int(input())
arr = list(map(int,input().split()))

new_arr = [0] * len(arr)
for i, a in enumerate(arr,1):
  new_arr[a-1] = i
print(*new_arr)
