S = int(input())

a = int(S/100 - (S%100)/100)
b = int(S%100)

if( 0<a<13 and 0<b<13 ):
  print("AMBIGUOUS")
if( (0<a<13 and 12<b<100) or (0<a<13 and b==0) ):
  print("MMYY")
if( (12<a<100 and 0<b<13) or (a==0 and 0<b<13) ):
  print("YYMM")
if( 12<a<100 and 12<b<100 ):
  print("NA")
if( a==0 and 12<b<100 ):
  print("NA")
if( 12<a<100 and b==0 ):
  print("NA")
if( a==0 and b==0 ):
  print("NA")


