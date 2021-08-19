n = int(input())
sum = 0.0
for i in range(1, n + 1):
    s = input().split()
    sum += float(s[1])
print(sum / n + 5)
