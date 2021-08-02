n, m = list(map(int, input().split()))
counter_list = [0] * (n + 1)
for i in range(m):
    a, b = list(map(int, input().split()))
    counter_list[a] += 1
    counter_list[b] += 1

for i in range(1, n + 1):
    print((counter_list[i]))
