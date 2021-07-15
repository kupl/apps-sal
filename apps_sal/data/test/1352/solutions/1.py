n, x = map(int, input().split())
a = list(map(int, input().split()))

mi = [x + 1] * (x + 1)
ma = [0] * (x + 1)
trie = [0] * (1 << 23)
m = 4
trie[0] = x + 1
for i in a:
  at = 0
  mii = x + 1
  maa = 0
  for j in range(19, -1, -1):
    if (i & (1 << j)):
      if not trie[at + 3]:
        trie[at + 3] = m
        at = m
        trie[m] = i
        trie[m + 1] = i
        m += 4
      else:
        at = trie[at + 3]
        trie[at] = min(trie[at + 0], i)
        trie[at + 1] = max(trie[at + 1], i)
    else:
      if trie[at + 3]:
        mii = trie[trie[at + 3]]
        if not maa:
          maa = trie[trie[at + 3] + 1]
      if not trie[at + 2]:
        trie[at + 2] = m
        at = m
        trie[m] = i
        trie[m + 1] = i
        m += 4
      else:
        at = trie[at + 2]
        trie[at] = min(trie[at + 0], i)
        trie[at + 1] = max(trie[at + 1], i)
  mi[i] = min(mi[i], mii)
  ma[i] = max(ma[i], maa)

fi = 0
for i in range(x, 0, -1):
  if mi[i] != x + 1:
    fi = i
    break

ans = 0
g = x + 1
for i in range(1, x + 1):
  ans += x - max(i, fi) + 1
  if i == g:
    break
  fi = max(fi, ma[i])
  g = min(g, mi[i])
print(ans)
