n = int(input())
cnt = [0] * (n + 1)
cmb = 0
a = list(map(int, input().split()))

for ai in a:
  cnt[ai] += 1
  cmb += cnt[ai] - 1

for ai in a:
  print((cmb - cnt[ai] + 1))

