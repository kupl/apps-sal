# 570_B

cases = int(input())

for i in range(0, cases):
    ln1 = [int(j) for j in input().split(" ")]
    nums = [int(j) for j in input().split(" ")]
    k = ln1[1]
    n1 = min(nums)
    n2 = max(nums)
    if n2 - n1 > k * 2:
        print(-1)
    else:
        print(max(n1 + k, n2 - k))
