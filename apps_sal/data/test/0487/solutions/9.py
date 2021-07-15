n = int(input())
num = list(map(int, input().split()))
x = max(num)
s = sum(num)
for i in range(x, 250):
    if i * n - s > s:
        print(i)
        break
