import string
n = int(input())
l = input()
r = input()
lefts = [[] for _ in range(256)]
rights = [[] for _ in range(256)]
oq = ord('?')
pairs = []
for i in range(n):
    lefts[ord(l[i])].append(i + 1)
    rights[ord(r[i])].append(i + 1)
q_store = [lefts[oq], rights[oq]]
q_used = [0, 0]
for c in string.ascii_lowercase:
    oc = ord(c)
    same_pairs = min(len(lefts[oc]), len(rights[oc]))
    for i in range(same_pairs):
        pairs.append((lefts[oc][i], rights[oc][i]))
    if same_pairs == len(rights[oc]):
        extras = lefts[oc]
        q_idx = 1
    else:
        extras = rights[oc]
        q_idx = 0
    for i in range(same_pairs, len(extras)):
        if q_used[q_idx] >= len(q_store[q_idx]):
            break
        if q_idx == 0:
            pairs.append((q_store[q_idx][q_used[q_idx]], extras[i]))
        else:
            pairs.append((extras[i], q_store[q_idx][q_used[q_idx]]))
        q_used[q_idx] += 1
while q_used[0] < len(q_store[0]) and q_used[1] < len(q_store[1]):
    pairs.append((q_store[0][q_used[0]], q_store[1][q_used[1]]))
    q_used[0] += 1
    q_used[1] += 1
print(len(pairs))
for pair in pairs:
    print(*pair)
