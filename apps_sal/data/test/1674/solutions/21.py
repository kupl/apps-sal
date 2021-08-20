(n, k) = map(int, input().split())
a = list(map(int, input().split()))
s = input() + '0'
i = S = 0
while i < n:
    pos1 = i
    while s[i + 1] == s[i]:
        i += 1
    pos2 = i
    d = pos2 - pos1 + 1
    if d <= k:
        S += sum(a[pos1:pos2 + 1])
    else:
        S += sum(sorted(a[pos1:pos2 + 1])[-k:])
    i += 1
print(S)
