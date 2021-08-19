n, m = map(int, input().split())
count = [0] * n
# print(count)
for i in range(m):
    a, b = map(int, input().split())
    count[a - 1] += 1
    count[b - 1] += 1
    # print(count)
for i in count:
    print(i)
