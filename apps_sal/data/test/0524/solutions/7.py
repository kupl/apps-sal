N = int(input())
arr = [int(x) for x in input().split()]
arr = sorted(arr)
MAX_NUM = 1e18

ans = 1e18
for i in range(1, 32000):
    curr = 0
    num = 1
    for j in range(N):
        curr += abs(arr[j] - num)
        num *= i
        if curr > MAX_NUM:
            break
    if curr > MAX_NUM:
        break
    ans = min(ans, curr)

print(ans)
