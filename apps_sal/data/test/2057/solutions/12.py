n = int(input())
list1 = list(map(int, input().split()))
time = [0] * (n + 1)
time[0] = 1
ans = 1
for i in range(n):
    if time[list1[i]] == 1:
        time[i + 1] = 1
        time[list1[i]] = 0
    else:
        ans += 1
        time[i + 1] = 1
print(ans)
