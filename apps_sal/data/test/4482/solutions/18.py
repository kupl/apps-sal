n = int(input())
a = list(map(int, input().split()))
avg_a = round(sum(a) / n)

result = 0
for num in a:
    result += (num - avg_a)**2

print(result)
