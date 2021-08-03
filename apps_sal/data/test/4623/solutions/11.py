t = int(input())
for _ in range(t):
    n = int(input())
    arr = [int(j) for j in input().split()]

    count = [0] * 101

    for x in arr:
        count[x] += 1

    ans = 0
    for i in range(1, 101):
        temp = 0
        for j in range(1, i + 1):
            temp += min(count[j], count[i - j])
        temp //= 2
        ans = max(ans, temp)
    print(ans)
