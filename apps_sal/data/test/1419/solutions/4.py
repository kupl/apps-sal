K = int( input() )
S = list( input().split() )

ans = -1
lb, ub = 1, int( 1e7 )
while lb <= ub:
  mid = lb + ub >> 1
  line, ptr, wptr = 0, 0, 0
  while ptr < len( S ):
    line += 1
    wid = 0
    while ptr < len( S ) and wid + len( S[ ptr ] ) + ( ptr + 1 < len( S ) ) - wptr <= mid:
      wid += len( S[ ptr ] ) + ( ptr + 1 < len( S ) ) - wptr
      ptr, wptr = ptr + 1, 0
    best = wptr # [ wptr, best )
    wnxt = wptr
    while ptr < len( S ) and wnxt < len( S[ ptr ] ) and wid + wnxt + 1 - wptr <= mid:
      if S[ ptr ][ wnxt ] == '-':
        best = wnxt + 1
      wnxt += 1
    wid += best - wptr
    wptr = best
    if ptr < len( S ) and wptr == len( S[ ptr ] ):
      ptr, wptr = ptr + 1, 0
    if wid == 0:
      line = 1 << 30
      break
  if line <= K :
    ans, ub = mid, mid - 1
  else:
    lb = mid + 1
print( ans )

