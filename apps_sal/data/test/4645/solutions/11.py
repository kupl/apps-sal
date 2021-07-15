t = int( input() )

for i in range( t ):
  n = int( input() )

  if n<=3:
    print( "-1" )
    continue

  ans = [ 2 , 4 , 1 , 3 ]

  m = 4
  idx = 1

  while m < n:
    m = m+1
    ans.append( m )

    m = m+1
    if m<=n:
      idx = 1
      while idx < len( ans ):
        if m-ans[idx-1] >= 2 and m-ans[idx-1]<=4 and m-ans[idx]>=2 and m-ans[idx]<=4:
          break
        idx = idx+1
      ans.insert( idx , m ) 

  for p in ans:
    print( p , end = " " )
  print( "\n" ) 


  
