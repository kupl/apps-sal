from math import *
dict1 = {}
n = int(input())
arr = list(map(int, input().split()))
for i in range(n):
    try:
        dict1[arr[i]] += 1
    except:
        KeyError
        dict1[arr[i]] = 1
ans = 0
for i in range(n):
    flag = 0
    for j in range(ceil(log2(arr[i])), 32):
        try:
            if pow(2, j) == 2 * arr[i]:
                if dict1[pow(2, j) - arr[i]] > 1:
                    flag = 1
                    break
            elif dict1[pow(2, j) - arr[i]] > 0:
                flag = 1
                break
        except:
            KeyError
    if flag == 0:
        ans += 1
print(ans)
