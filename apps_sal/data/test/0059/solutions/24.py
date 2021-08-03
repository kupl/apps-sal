n = int(input())
a = list(map(int, input().split(" ")))
s = list(map(int, input()))
right = [-1] * n
i = n - 2
right[n - 1] = n - 1
if s[i] == 1:
    right[i] = i + 1
else:
    right[i] = i
i -= 1
while i >= 0:
    if s[i] == 0:
        right[i] = i
    else:
        if s[i + 1] == 0:
            right[i] = i + 1
        else:
            right[i] = right[i + 1]
    i -= 1

ans = True
i = 0
for ai in a:
    if ai - 1 > right[i]:
        ans = False
    i += 1

print("YES" if ans else "NO")
