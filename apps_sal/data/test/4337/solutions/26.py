input()
s = map(str,input().split())
print("Three" if len(set(s))==3 else "Four")
