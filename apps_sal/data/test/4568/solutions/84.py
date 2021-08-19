n = int(input())
s = list(input())
ans = []
for i in range(1, n):
    first_falf = set(s[:i])
    after_falf = set(s[i:])
    count = 0
    for word in first_falf:
        if word in after_falf:
            count += 1
    ans.append(count)
print(max(ans))
