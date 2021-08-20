n = int(input())
s = list(input())
prev = s[0]
counter = 0
for item in s:
    if item == prev:
        counter += 1
    else:
        break
s.reverse()
counter1 = 0
prev1 = s[0]
for item in s:
    if item == prev1:
        counter1 += 1
    else:
        break
if prev == prev1:
    print((counter + 1) * (counter1 + 1) % 998244353)
else:
    print(counter + counter1 + 1 % 998244353)
