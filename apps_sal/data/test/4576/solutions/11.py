a = int(input())
b = int(input())
c = int(input())
x = int(input())

cnt = 0

for a_idx in range(a + 1):
  for b_idx in range(b + 1):
    for c_idx in range(c + 1):
      total = 500 * a_idx + 100 * b_idx + 50 * c_idx
      if (total == x): cnt += 1

print(cnt)
