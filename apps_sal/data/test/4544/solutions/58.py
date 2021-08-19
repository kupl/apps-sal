n = int(input())
a = sorted(list(map(int, input().split(' '))))
counter = [0 for i in range(10 ** 5 + 2)]
ans = 0
for i in range(n):
    counter[a[i]] += 1
for i in range(1, 10 ** 5 + 1):
    temp = sum(counter[i - 1:i + 2])
    ans = max(ans, temp)
print(ans)
