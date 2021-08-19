s = input()
l = input()
k = int(input())
no_bad = []
curr = 0
p = 31
m = 67280421310721
hashes = []
currh = 0
cnt = 0
P = [pow(p, i, m) for i in range(len(s) + 2)]
for i in s:
    currh += P[cnt] * ord(i) % m
    cnt += 1
    hashes.append(currh)
    if l[ord(i) - ord('a')] == '0':
        no_bad.append(curr + 1)
        curr += 1
    else:
        no_bad.append(curr)
no_bad.append(0)
hashes.append(0)
ans = set()
for i in range(len(s)):
    for j in range(i, len(s)):
        if no_bad[j] - no_bad[i - 1] <= k:
            has = (hashes[j] - hashes[i - 1]) * P[len(s) - i + 1] % m
            ans.add(has)
print(len(ans))
