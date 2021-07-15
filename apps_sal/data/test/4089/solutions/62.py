n=int(input()); s='';
while n>0:
  n-=1; s+=chr(97+n%26); n//=26;
print(s[::-1])
