n, k = map(int, input().split())
s = list(input())
if not k:
    print(''.join(s))
    return

if n == 1:
    print(0)
    return

if s[0] != '1':
    s[0] = '1'
    k -= 1
if not k:
    print(''.join(s))
    return

for i in range(1, n):
    if s[i] == '0':
        continue
    s[i] = '0'
    k -= 1
    if not k:
        break

print(''.join(s))
