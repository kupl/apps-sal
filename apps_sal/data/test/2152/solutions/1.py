n = int(input())
mini = 10 ** 9 + 7
sum = 0
for i in range(n):
    a, p = list(map(int, input().split()))
    mini = min(mini, p)
    sum += mini * a
print(sum)
