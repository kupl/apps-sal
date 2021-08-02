n = int(input())

arr = [int(x) for x in input().split(" ")]

ans = 0

sum = 0

curr = True

for i in range(len(arr)):
    if ((sum + arr[i]) == 0 or ((sum + arr[i]) > 0) == curr):
        if curr:
            temp = -1 - sum
        else:
            temp = 1 - sum
        ans += abs(temp - arr[i])
        sum += temp
    else:
        sum += arr[i]
    curr = not curr

ans1 = 0

curr = False

sum = 0

for i in range(len(arr)):
    if ((sum + arr[i]) == 0 or ((sum + arr[i]) > 0) == curr):
        if curr:
            temp = -1 - sum
        else:
            temp = 1 - sum
        ans1 += abs(temp - arr[i])
        sum += temp
    else:
        sum += arr[i]
    curr = not curr

print(min(ans, ans1))
