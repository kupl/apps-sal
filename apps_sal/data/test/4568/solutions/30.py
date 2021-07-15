n = int(input())
s = input()
count = 0
ans = 0
for i in range(0, n - 1):
    x = list(s[:i + 1])
    y = list(s[i + 1:])
    for c in range(ord('a'), ord('z') + 1):
        if chr(c) in x and chr(c) in y:
            count += 1
    if ans < count:
        ans = count
    count = 0
print(ans)
