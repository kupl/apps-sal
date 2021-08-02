n, k = map(int, input().split())
s = input()
sl = []
for i in range(n):
    if i + 1 == k:
        sl.append(s[i].lower())
    else:
        sl.append(s[i])
print(''.join(sl))
