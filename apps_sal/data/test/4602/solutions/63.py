n = int(input())
k = int(input())
x = list(map(int, input().split()))
c = 0
for i in range(len(x)):
    c += min(x[i], k - x[i]) * 2
print(c)
