n = int(input())
s = input()
count = 0
i = 1
while i < n:
    if s[i] == s[i - 1]:
        count += 1
    i += 1
print(count)
