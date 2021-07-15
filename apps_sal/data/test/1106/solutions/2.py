def result(i):
    nonlocal ans
    temp = 0
    if i < (1 << n):
        temp = (result(2 * i), result(2 * i + 1))
        ans += abs(temp[0] - temp[1])
        temp = max(temp)
    return lights[i] + temp

n = int(input())
lights = [0, 0] + list(map(int, input().split()))
ans = 0
result(1)
print(ans)

