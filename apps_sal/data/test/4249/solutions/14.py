(n, m) = list(map(int, input().split()))
l = list(map(int, input().split()))
l.sort(reverse=True)
left = 1
right = n


def check(k, m):
    if m > 0:
        lef = 0
        z = 0
        for i in range(n):
            m -= max(0, l[i] - lef)
            z += 1
            if z == k:
                z = 0
                lef += 1
    if m <= 0:
        return 1
    else:
        return 0


res = []
while left <= right:
    mid = int((left + right) / 2)
    if check(mid, m):
        res.append(mid)
        right = mid - 1
    else:
        left = mid + 1
if len(res) > 0:
    print(min(res))
else:
    print('-1')
'\nn, m = map(int, input().split())\n\nl = list(map(int,input().split()))\n\ns = sum(l)\nans = 0\n\ndef find(x):\n  su = 0\n  days = 0\n  z = 0\n\n  for i in l:\n    su += max(0, i-z)\n    days += 1\n    if days == x:\n      days = 0\n      z += 1\n  if su < m:\n    return 0\n  return x\n\ndef binary(left, right):\n  nonlocal ans\n  mid = int((left+right)/2)\n  r = find(mid)\n  if right == left:\n    ans = r\n  elif left == right - 1:\n    if r:\n      ans = r\n    else:\n      binary(r, r)\n  else:\n    if r:\n      binary(left, mid)\n    else:\n      binary(mid, right)\n\nif s < m:\n  print("-1")\nelif s == m:\n  print(n)\nelse:\n  l.sort(reverse = True)\n  binary(1,n)\n  print(ans)\nprint(ans)\n'
