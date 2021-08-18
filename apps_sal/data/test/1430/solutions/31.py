import itertools
n, k = list(map(int, input().split()))
s = input()
d = []

if s[0] == "0":
    zero = True
    iti = False
else:
    iti = True
    zero = False

count = 0
for i in range(0, len(s)):
    if zero and s[i] == "0":
        count += 1
    elif zero and s[i] == "1":
        d.append(count)
        iti = True
        zero = False
        count = 1
    elif iti and s[i] == "0":
        d.append(count)
        zero = True
        iti = False
        count = 1
    elif iti and s[i] == "1":
        count += 1
d.append(count)
d.append(0)
acum = list(itertools.accumulate([0] + d))
hantei = 0
ans = 0
if s[0] == "0":
    ks1 = min(k * 2, len(d))
    ks2 = min(k * 2 + 1, len(d))
else:
    ks1 = min(k * 2 + 1, len(d))
    ks2 = min(k * 2, len(d))

for i in range(0, len(d) - ks1 + 1, 2):
    ans = max(acum[i + (ks1)] - acum[i], ans)
for i in range(1, len(d) - ks2 + 1, 2):
    ans = max(acum[i + (ks2)] - acum[i], ans)
print(ans)
