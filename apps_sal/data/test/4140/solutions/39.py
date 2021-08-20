s = input()
odd_0 = 0
odd_1 = 0
even_0 = 0
even_1 = 0
for i in range(len(s)):
    if i % 2 == 0:
        if s[i] == '0':
            odd_0 += 1
        else:
            odd_1 += 1
    elif s[i] == '0':
        even_0 += 1
    else:
        even_1 += 1
a = odd_0 + even_1
b = odd_1 + even_0
ans = min(a, b)
print(ans)
