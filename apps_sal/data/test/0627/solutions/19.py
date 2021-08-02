n = int(input())
s = [*input()]
for i in range(n):
    if i == n - 1 or s[i] > s[i + 1]:
        del s[i]
        break
print(''.join(s))
