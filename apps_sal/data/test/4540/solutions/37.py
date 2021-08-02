n = int(input())
lis = [0] + list(map(int, input().split())) + [0]

s = 0
for i in range(n + 1):
    tmp = abs(lis[i] - lis[i + 1])
    s += tmp

for i in range(1, n + 1):
    ans = s + abs(lis[i - 1] - lis[i + 1]) - (abs(lis[i - 1] - lis[i]) + abs(lis[i] - lis[i + 1]))
    print(ans)
