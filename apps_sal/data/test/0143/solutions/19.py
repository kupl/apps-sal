n = int(input())
arr = [int(x) for x in input().split()]
arr.sort()
point = 0
for i in range(n):
    if(point < arr[i]):
        point += 1
print(point + 1)
