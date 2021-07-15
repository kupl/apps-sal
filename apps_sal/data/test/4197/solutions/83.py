N = int(input())
arr = list(map(int, input().split()))
arr2 = [0]*N
for i in range(N):
    arr2[arr[i]-1] = i+1
print(*arr2)
