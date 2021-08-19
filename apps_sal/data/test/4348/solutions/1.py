(n, k) = map(int, input().split())
s = input()
dic = dict()
for item in s:
    if item not in dic:
        dic[item] = 1
    else:
        dic[item] += 1
alphabet = 'abcdefghijklmnopqrstuvwxyz'
en = ''
for item in alphabet:
    if item not in dic:
        continue
    if dic[item] <= k:
        k -= dic[item]
    else:
        en = item
        break
ans = ''
for item in s:
    if item > en:
        ans += item
    elif item == en and k == 0:
        ans += item
    elif item == en and k > 0:
        k -= 1
if en == '':
    print()
else:
    print(ans)
