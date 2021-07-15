MOD = 10**9 + 7
p3 = [1]

S = input()
n = len(S)

a = []
c = []
q = []
for i in range(n):
  p3.append(int(p3[i] * 3 % MOD))
  if S[i] == 'A':
    a.append(1)
  else:
    a.append(0)
  if S[i] == 'C':
    c.append(1)
  else:
    c.append(0)
  if S[i] == '?':
    q.append(1)
  else:
    q.append(0)

for i in range(1, n):
  a[i] += a[i - 1]
  c[i] += c[i - 1]
  q[i] += q[i - 1]

count = 0
for i in range(1, n - 1):
  if S[i] == 'B' or S[i] == '?':
    bq = 0 if S[i] == 'B' else 1
    count += a[i - 1] * (c[n - 1] - c[i]) * p3[q[n - 1] - bq]
    count += q[i - 1] * (c[n - 1] - c[i]) * p3[q[n - 1] - 1 - bq]
    count += a[i - 1] * (q[n - 1] - q[i]) * p3[q[n - 1] - 1 - bq]
    count += q[i - 1] * (q[n - 1] - q[i]) * p3[q[n - 1] - 2 - bq]

print((int(count % MOD)))

