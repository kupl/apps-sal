def main():
  a = [int(x) for x in input().split()]
  g = 1
  mo = 0
  w = 1
  bigarray = [0]* 1000000
  rmo = []
  req = a[1]
  seq = [int(x) for x in input().split()]
  bigarray[seq[0]] += 1
  first = 0
  last = 0
  if a[0] == req:
    rmo = [1, a[0]]
  else:
    while first != len(seq) - 1:
      if w < req:
        if bigarray[seq[first + 1]] == 0:
          first += 1
          bigarray[seq[first]] += 1
          g = g + 1
          w = w + 1
        elif bigarray[seq[first + 1]] != 0:
          bigarray[seq[first + 1]] += 1
          first = first + 1
          g = g + 1
        if mo < g:
          mo = g
          rmo = [last + 1, first + 1]
      elif w >= req:
        if bigarray[seq[first + 1]] == 0:
          bigarray[seq[last]] -= 1
          if bigarray[seq[last]] == 0:
            w = w - 1
          if g > mo:
            mo = g
            rmo = [last + 1, first + 1]
          g = g - 1
          last = last + 1
        else:
          g = g + 1
          first += 1
          bigarray[seq[first]] += 1
          if mo < g:
            mo = g
            rmo = [last + 1, first + 1]
  for x in rmo:
    print(x, end = ' ')
main() 
