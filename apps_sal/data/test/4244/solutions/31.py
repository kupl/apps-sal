n = int(input())
x = list(map(int, input().split()))
s = 0
for i in x:
    s += i
p = int(s / n + 0.5)
result = 0
for i in x:
    result += (i - p) ** 2
print(result)
