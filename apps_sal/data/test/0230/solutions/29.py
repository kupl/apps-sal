n = int(input())
s = input()

a = 0
i = 0
j = 1
while j < n:
    if s[i:j] in s[j:]:
        a = max(a, j - i)
        j += 1
    else:
        i += 1

    if i == j:
        i += 1
        j += 2
print(a)
