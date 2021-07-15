abcd = []
max_ans = 0

def resolve(l):
  total = 0
  for a, b, c, d in abcd:
    if l[b-1] - l[a-1] == c:
      total += d

  return total

def comb(l, start, end, now, suspend):
  nonlocal max_ans
  if now == suspend:
    max_ans = max([max_ans, resolve(l)])
    return

  for i in range(start, end+1, 1):
    comb(l + [i], i, end, now+1, suspend)


n, m, q = list(map(int, input().split()))

for i in range(q):
  abcd.append(list(map(int, input().split())))

comb([], 1, m, 0, n)

print(max_ans)


