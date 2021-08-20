n = int(input())
a = input()
s = set()
ans = 0
for j in range(n):
    if a[j] == 'R':
        if 'L' in s:
            ans += 1
            s = set()
        s.add(a[j])
    elif a[j] == 'L':
        if 'R' in s:
            ans += 1
            s = set()
        s.add(a[j])
    elif a[j] == 'U':
        if 'D' in s:
            ans += 1
            s = set()
        s.add(a[j])
    elif a[j] == 'D':
        if 'U' in s:
            ans += 1
            s = set()
        s.add(a[j])
print(ans + 1)
