(n, x) = list(map(int, input().split()))
l_list = [int(i) for i in input().split()]
d = 0
count = 1
for i in range(n):
    d = d + l_list[i]
    if d <= x:
        count += 1
print(count)
