import sys
input = sys.stdin.readline
from collections import Counter
def f():
  n = int(input())
  A = tuple(map(int, input().split()))
  if n%2:
    return False
  C = Counter(A)
  for v in C.values():
    if v%2:
      return True
  return False
t = int(input())
for _ in range(t):
  if f():
    print("First")
  else:
    print("Second")
