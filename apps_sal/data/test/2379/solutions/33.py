line1 = input().split()
n = int(line1[0])
k = int(line1[1])
c = int(line1[2])
s = list(input())
l = [s.index("o") + 1]
r = [len(s) - s[::-1].index("o")]
for i in range(1, k):
  j = l[i - 1]
  m = r[i - 1]
  while j - l[i - 1] <= c or s[j - 1] != "o":
    j += 1
  while r[i - 1] - m <= c or s[m - 1] != "o":
    m -= 1
  r.append(m)
  l.append(j)
r = r[::-1]
for i in range(len(r)):
  if r[i] == l[i]:
    print(r[i])
