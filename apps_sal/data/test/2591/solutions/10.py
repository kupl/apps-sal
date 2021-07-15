t = int(input())

for _ in range(t):
    n = int(input())
    As = list(map(int, input().split()))
    As.sort()
    left = 0
    right = n-1
    res = []
    while left <= right:
        if left == right:
            res.append(As[left])
            break
        res.append(As[right])
        res.append(As[left])
        right -= 1
        left += 1
    print(" ".join(map(str, res[::-1])))

