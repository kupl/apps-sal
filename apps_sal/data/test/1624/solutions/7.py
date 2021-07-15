n = int(input())
s = sorted(list(map(int, input().split())))
answer = 0
for i in range(n // 2):
    answer += (s[i] + s[n - i - 1]) ** 2
print(answer)

