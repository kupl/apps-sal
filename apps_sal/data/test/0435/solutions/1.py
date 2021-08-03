n, k = list(map(int, input().split()))
s = input()

longest = 0

left, right = 0, 0
currb = 1 if s[0] == 'b' else 0
while True:
    while right < n and currb <= k:
        right += 1
        if right < n and s[right] == 'b':
            currb += 1
    longest = max(longest, right - left)
    if s[left] == 'b':
        currb -= 1
    left += 1
    if left == n or right == n:
        break

left, right = 0, 0
currb = 1 if s[0] == 'a' else 0
while True:
    while right < n and currb <= k:
        right += 1
        if right < n and s[right] == 'a':
            currb += 1
    longest = max(longest, right - left)
    if s[left] == 'a':
        currb -= 1
    left += 1
    if left == n or right == n:
        break

print(longest)
