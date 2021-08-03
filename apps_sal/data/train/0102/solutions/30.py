t = int(input())
arr = []
while t > 0:
    t -= 1
    n = int(input())
    ans = 9 * (len(str(n)) - 1)
    for i in range(1, 10):
        if int(str(i) * len(str(n))) <= n:
            ans += 1
    arr.append(ans)
print(*arr, sep="\n")
