w = input()
ans = 'Yes'
if len(w) % 2 == 1:
    ans = 'No'
else:
    s = sorted(w)
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            if count % 2 == 1:
                ans = 'No'
                break
            count = 1
print(ans)
