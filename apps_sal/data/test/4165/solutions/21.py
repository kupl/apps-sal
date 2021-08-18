N = int(input())
len = list(map(int, input().split()))


short_len = sum(len) - max(len)
result = 'Yes' if short_len > max(len) else 'No'
print(result)
