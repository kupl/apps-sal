# 2 3  : 2 -> 3
# 1 1 : done
# 3 6 : 3 -> 2, 2 -> 3 går inte högre (nej)
# 6 8 : 6 -> 9 - JA
# 1 2 : nej
# 4 1 : ja
# 31235 6578234 : antagligen

# Om över 10 - verkar alltid gå

# 1 - bara 1
# 2 - 1, 2, 3
# 3 - 1, 2, 3
# 4 -> 6 -> 9 -> 8 -> 12 -> 18 -> 27 (verkar gå att fly)

def possible(x, y):
  if x >= 4: return True
  if x == 3: return y <= 3
  if x == 2: return y <= 3
  if x == 1: return y == 1

t = int(input())
for _ in range(t):
  a, b = [int(x) for x in input().split()]
  print("YES" if possible(a, b) else "NO")

