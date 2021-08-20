n = int(input())
s = input()
count = []
for i in range(1, n):
    first = s[:i]
    second = s[i:]
    count.append(len(set(first) & set(second)))
print(max(count))
