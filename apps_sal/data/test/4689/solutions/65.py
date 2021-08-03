k, n = map(int, input().split())
a_list = list(map(int, input().split()))
longest = 0
for i in range(n):
    if i == n - 1:
        longest = max(longest, k - a_list[i] + a_list[0])
    else:
        distance = a_list[i + 1] - a_list[i]
        longest = max(longest, distance)
print(k - longest)
