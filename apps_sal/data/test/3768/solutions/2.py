def solve(a, b):
  r = []
  while a and b and a+b > 2:
    q = min((a//b + b//a), max(a, b)-1)
    r.append(str(q))
    if a > b:
      r.append('A')
      a -= b*q
    else:
      r.append('B')
      b -= a*q
  if a != 1 or b != 1:
    return 'Impossible'
  return ''.join(r)

def main():
  a, b = map(int, input().split())
  print(solve(a, b))

main()
