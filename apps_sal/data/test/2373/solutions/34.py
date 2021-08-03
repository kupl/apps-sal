n = int(input())
p = list(map(int, input().split()))
num_list = [0] * (n + 1)

for i in range(n):
    if p[i] == i + 1:
        num_list[p[i] - 1] = 1

counter = 0
res = 0
for i in range(n + 1):
    if num_list[i] == 1:
        counter += 1
    else:
        res += (counter + 2 - 1) // 2
        counter = 0

print(res)
