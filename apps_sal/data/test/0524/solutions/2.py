n = int(input())
arr = sorted(list(map(int, input().split())))

ans = sum(arr) - n

for i in range(2, 10 ** 9):
    if abs(i ** (n - 1) - arr[-1]) > ans:
        break

    ans2 = 0
    for j in range(0, n):
        ans2 += abs(i ** j - arr[j])

    ans = min(ans, ans2)

print(ans)

