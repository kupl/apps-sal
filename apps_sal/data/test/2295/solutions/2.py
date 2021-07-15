n = int(input())
arr = [0]
arr = arr + list(map(int, input().split(' ')))

def getCounts(arr):
    last = {}
    ans = 0.0
    prev = 0.0
    res = 0.0
    for i in range(1, len(arr)):
        if arr[i] not in last:
            ans = prev + i
        else:
            ans = prev + i - last[arr[i]]
        prev = ans
        res += ans
        last[arr[i]] = i
    return res

ans = (2 * getCounts(arr) - n)/(n*n)
print("%.6f" % ans)

