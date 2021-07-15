n, x = tuple(map(int, input().split()))
arr = list(map(int, input().split()))

arr += arr[::]
arr2 = [i * (i + 1) // 2 for i in arr]

ans = 0
for now_month in range(n, n * 2):
    if now_month == n:
        last_month = now_month
        count_obnim = 0
        count_days = 0
        while count_days + arr[last_month] <= x:
            count_days += arr[last_month]
            count_obnim += arr2[last_month]
            last_month -= 1

        dop_days = x - count_days
        nodop_days = arr[last_month] - dop_days
        dop_obnim = arr2[last_month] - nodop_days * (nodop_days + 1) // 2
        count_days += dop_days
        count_obnim += dop_obnim
    else:
        count_days += arr[now_month]
        count_days -= dop_days
        count_obnim += arr2[now_month]
        count_obnim -= dop_obnim

        while count_days > x:
            count_days -= arr[last_month + 1]
            count_obnim -= arr2[last_month + 1]
            last_month += 1

        dop_days = x - count_days
        nodop_days = arr[last_month] - dop_days
        dop_obnim = arr2[last_month] - nodop_days * (nodop_days + 1) // 2
        count_days += dop_days
        count_obnim += dop_obnim

    ans = max(ans, count_obnim)

print(ans)

