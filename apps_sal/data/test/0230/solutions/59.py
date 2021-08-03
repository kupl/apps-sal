n = int(input())
s = input()
j = 1
result = [0]
end = n // 2 + 1
for i in range(n):
    while (j < n - 1) and (s[i:j] in s[:i] + "0" + s[j:]):
        j += 1
    result.append(j - i - 1)
print(max(result))
