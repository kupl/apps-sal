n = int(input())
s = input()

right = 0
ans = 0
for left in range(n):
    while right < n:
        word = s[left:right + 1]
        if word in s[right + 1:]:
            ans = max(ans, len(word))
        else:
            break
        right += 1

print(ans)
