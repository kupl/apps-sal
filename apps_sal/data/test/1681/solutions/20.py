a = input()
b = input()
x = [0] * 26
y = [0] * 26
for c in a:
    x[ord(c) - ord('a')] += 1
for c in b:
    y[ord(c) - ord('a')] += 1
result = 0
for i in range(26):
    if x[i] == 0 and y[i] > 0:
        result = -1
        break
    result += min(x[i], y[i])
print(result)
