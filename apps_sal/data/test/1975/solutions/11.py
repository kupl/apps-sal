input_list = [int(i) for i in input().split()]
n = input_list[0]
m = input_list[1]
print(n + m - 1)
for i in range(1, m + 1):
    print(1, i)
for i in range(2, n + 1):
    print(i, m)
