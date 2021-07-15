n = int(input())
l = [0] + list(map(int, input().split()))
res = 0
for i in range(n):
    res += abs(l[i] - l[i + 1])
print(res)
