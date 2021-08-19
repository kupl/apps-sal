t = input().strip()
t = [int(e) for e in t.split(' ')]
n = t[0]
k = t[1]
s = input()
assert len(s) == n
sum_l = [0 for i in range(26)]
for c in s:
    sum_l[ord(c) - ord('a')] += 1
need_l = [0 for i in range(26)]
for i in range(26):
    if k <= sum_l[i]:
        need_l[i] = k
        break
    else:
        need_l[i] = sum_l[i]
        k -= need_l[i]
result = []
for c in s:
    index = ord(c) - ord('a')
    if need_l[index] > 0:
        need_l[index] -= 1
    else:
        result.append(c)
print(''.join(result))
