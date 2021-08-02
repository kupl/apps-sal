s = input()

ans = True

if s != s[::-1]:
    print('No')
    return

n = len(s)
m = int((n - 1) / 2)
s_2 = s[0:m]

if s_2 != s_2[::-1]:
    print('No')
    return

l = int((n + 3) / 2) - 1
s_3 = s[l:]

if s_3 != s_3[::-1]:
    print('No')
    return

print('Yes')
