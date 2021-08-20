n = int(input())
s = input()
max_len = 0
j = 0
for i in range(n):
    while j < n and s[i:j] in s[j:]:
        j += 1
    max_len = max(max_len, j - i - 1)
print(max_len)
