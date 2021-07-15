n=int(input())
if n%3==0:
 print('yes')
elif n//3%2==0 and n%3==1:
 print('yes')
else:
 print('no')
