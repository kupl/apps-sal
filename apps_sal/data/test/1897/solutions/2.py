string = input().strip()
s = [0]
for c in string:
    s.append(s[-1] + (c in 'IEAOUY'))
result, cur = 0, 0
for l in range(1, len(string) + 1):
    cur += s[-l] - s[l - 1]
    result += cur / l
print(result)
