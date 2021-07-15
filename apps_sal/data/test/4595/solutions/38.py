s=input()
b=s.index("A")
a=[i for i, x in enumerate(s) if x == 'Z']
print(a[-1]-b+1)
