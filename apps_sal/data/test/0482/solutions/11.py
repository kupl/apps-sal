import string
alphabet = string.ascii_lowercase
(n, k) = map(int, input().split())
le = min(k, 26)
index = 0
result = ''
for i in range(1, n + 1):
    result += alphabet[int(index)]
    index += 1
    if index >= k:
        index = 0
print(result)
