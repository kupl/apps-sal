n = int(input())
s = input()
max_count = 0
for i in range(1, n):
    s1 = ''.join(set(s[:i]))
    s2 = ''.join(set(s[i:]))
    count = 0
    for j in range(len(s1)):
        if s1[j] in s2:
            count += 1
    if count > max_count:
        max_count = count
print(max_count)
