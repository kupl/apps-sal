n = int(input())
numbers = list(map(int, input().split()))
numbers = sorted(numbers)
ans = 0
for i in range(n // 2):
    ans += (numbers[i] + numbers[n - i - 1]) ** 2
print(ans)
