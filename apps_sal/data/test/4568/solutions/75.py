N = int(input())
s = input()

result = 0
for i in range(N - 1):
    a = set(s[:i])
    b = set(s[i:])
    result = max(result, len(a & b))

print(result)
