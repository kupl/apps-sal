n, S = [int(x) for x in input().split()]

A = [int(x) for x in input().split()]

def ans():
  nonlocal S
  to_min = sum(A) - n*min(A)
  S -= to_min
  if S <= 0:
    return min(A)
  if n*min(A) < S: return -1
  return (n*min(A) - S) // n

print(ans())

