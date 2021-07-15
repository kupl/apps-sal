from collections import Counter
s = input()
count = Counter(s)
ans = 0
for i in s[::-1]:
    if i == 'g':
        if count['g'] >= count['p'] + 2:
            ans += 1
            count['g'] -= 1
            count['p'] += 1
print(ans)
