number, time = map(int, input().split())
if time >= number // 2:
    ans = (number - 1) * number // 2
else:
    ans = (number - 1 + number - time) * time // 2
    count = time
    for i in range(time + 1, number):
        ans += count
        if i >= number - time:
            count -= 1
print(ans)
