n = int(input())
set1 = set()
ans = 0
for i in range(97, 123):
    set1.add(chr(i))
for i in range(n):
    (a, b) = input().split()
    if len(set1) == 1:
        if a == '?' and i != n - 1:
            ans += 1
        if a == '!':
            ans += 1
    else:
        set2 = set()
        for i in b:
            set2.add(i)
        if a == '.':
            set1 -= set2
        elif a == '!':
            set1 &= set2
        elif a == '?':
            set1 -= set2
print(ans)
