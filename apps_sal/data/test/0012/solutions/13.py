n = int(input())
s = input()
max = 0
l = 0
has_s = False
gs = 0
for r in range(n):
    if s[r] == 'G':
        gs += 1
    else:
        if not has_s:
            has_s = True
        else:
            while s[l] == 'G':
                l += 1
            l += 1
    if r - l + 1 > max:
        max = r - l + 1
ans = max
if gs < max:
    ans -= 1

print(ans)
