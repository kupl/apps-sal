import math
n = int(input())
arr = list(map(int, input().split()))
even = []
odd = []
for i in range(n):
    if arr[i] % 2 == 0:
        even.append(arr[i])
    else:
        odd.append(arr[i])
if abs(len(even) - len(odd)) <= 1:
    print(0)
    return
if len(even) > len(odd):
    even.sort(reverse=True)
    ans = 0
    for i in range(len(odd) + 1, len(even)):
        ans += even[i]
    print(ans)
    return
odd.sort(reverse=True)
ss = 0
for i in range(len(even) + 1, len(odd)):
    ss += odd[i]
print(ss)
