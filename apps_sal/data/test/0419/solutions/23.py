n = int(input(), 2)
a = [1]
for i in range(200):
  a.append(a[-1] * 4)
for i in range(200):
  if a[i] >= n:
    print(i)
    break

