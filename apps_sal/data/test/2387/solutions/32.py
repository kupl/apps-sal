import sys
input = sys.stdin.readline

def main():
  n = int(input())
  
  a = []
  b = []
  for i in range(n):
    s = input()
    c1, c2 = 0, 0
    for i in range(len(s)):
      if s[i] == "(":
        c2 += 1
      if s[i] == ")":
        if c2:
          c2 -= 1
        else:
          c1 += 1
    if c1 >= c2:
      b.append((c2, c1))
    else:
      a.append((c1, c2))
  a.sort()
  b.sort(reverse=True)
  ans = False
  sub = 0
  for value in a:
    k1, k2 = value[0], value[1]
    if sub < k1:
      ans = True
      break
    sub += k2-k1
  for value in b:
    k2, k1 = value[0], value[1]
    if ans or sub < k1:
      ans = True
      break
    sub += k2-k1
  print("No" if ans or sub else "Yes")

def __starting_point():
  main()
__starting_point()
