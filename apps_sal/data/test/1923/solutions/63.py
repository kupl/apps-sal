n = int(input())
num = [int(i) for i in input().split(' ')]
num.sort(reverse=True)
m = 0
for i in range(1, n + 1):
    m += num[2 * i - 1]
print(m)
