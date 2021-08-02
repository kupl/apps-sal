n = int(input())
p = list(map(int, input().split()))

count = 0

for i in range(1, n - 1):
    a_list = [p[i - 1], p[i], p[i + 1]]
    b_list = sorted(a_list)

    if a_list[1] == b_list[1]:
        count += 1

print(count)
