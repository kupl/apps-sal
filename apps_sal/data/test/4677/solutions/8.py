buf=''
for c in input():
  if c=='B': buf=buf[:-1]
  else: buf += c
print(buf)
