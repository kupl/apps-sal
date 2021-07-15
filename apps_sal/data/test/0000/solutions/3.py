import sys
s = input()
st = s.find('[')
if st==-1: print((-1)); return
s = s[st+1:]
#print(s)
st = s.find(':')
if st==-1: print((-1)); return
s = s[st+1:]
#print(s)
s = s[::-1]
st = s.find(']')
if st==-1: print((-1)); return
s = s[st+1:]
#print(s)
st = s.find(':')
if st==-1: print((-1)); return
s = s[st+1:]
#print(s)
x = s.count('|')
print(x+4 if x>=0 else -1)

