import sys
import math
input = sys.stdin.readline

n = int(input())

arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))
    arr[-1].append(i + 1)

ans = []
arr.sort()
# print(arr)
done = [0] * n
i = 0
j = 1
while i < n and j < n:
    if arr[i][0] == arr[j][0] and arr[i][1] == arr[j][1]:
        ans.append([arr[i][3], arr[j][3]])
        done[arr[i][3] - 1] += 1
        done[arr[j][3] - 1] += 1
        i += 2
        j += 2
    else:
        i += 1
        j += 1
# print(ans)
# print(done)
arr1 = []
for i in range(n):
    if done[arr[i][3] - 1] == 0:
        arr1.append(arr[i])
n = len(arr1)
# print("arr1",arr1)
i = 0
j = 1
while i < n and j < n:
    if arr1[i][0] == arr1[j][0]:
        ans.append([arr1[i][3], arr1[j][3]])
        done[arr1[i][3] - 1] += 1
        done[arr1[j][3] - 1] += 1
        i += 2
        j += 2
    else:
        i += 1
        j += 1
# print(ans)
arr2 = []
#print("arr1", arr1)
for i in range(n):
    if done[arr1[i][3] - 1] == 0:
        arr2.append(arr1[i])
# print(done)
n = len(arr2)
# print(arr2)
for i in range(n):
    if i % 2 == 0:
        ans.append([arr2[i][3], arr2[i + 1][3]])

for i in range(len(ans)):
    print(*ans[i])
