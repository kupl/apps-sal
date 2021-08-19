n = int(input())
lis = list(map(int, input().split()))
total = 0
for i in lis:
    x = 1 / i
    total += x
print(1 / total)
