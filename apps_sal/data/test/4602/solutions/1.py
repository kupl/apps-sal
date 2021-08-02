n = int(input())
k = int(input())
li = list(map(int, input().split()))

dis = 0
for i in range(n):
    dis += min(2 * li[i], 2 * abs(li[i] - k))

print(dis)
