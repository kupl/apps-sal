k, n = map(int, input().split())
a_list = list(map(int, input().split()))
longest = 0

for i in range(n - 1):
    distance = a_list[i + 1] - a_list[i]
    longest = max(longest, distance)

print(k - max(longest, k - a_list[n - 1] + a_list[0]))
