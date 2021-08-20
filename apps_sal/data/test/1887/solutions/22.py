n = int(input())
first = list(map(int, input().split()))
second = list(map(int, input().split()))
dp_first = [0] * n
dp_second = [0] * n
dp_first[0] = first[0]
dp_second[0] = second[0]
for i in range(1, n):
    dp_first[i] = max(dp_first[i - 1], first[i] + dp_second[i - 1], first[i] + dp_second[i - 2] if i >= 2 else 0)
    dp_second[i] = max(dp_second[i - 1], second[i] + dp_first[i - 1], second[i] + dp_first[i - 2] if i >= 2 else 0)
print(max(dp_first[-1], dp_second[-1]))
