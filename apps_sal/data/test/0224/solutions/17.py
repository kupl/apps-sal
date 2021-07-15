s = "A" + input() + 'A'

counter = 0
ans = 0
last = 0

for i in range(1, len(s)):
    if s[i] in "AEIOUY":
        counter = i - last
        last = i
        if counter > ans:
            ans = counter

print(ans)

