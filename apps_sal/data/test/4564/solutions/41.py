s = list(map(str,input()))
print("yes" if len(s) == len(set(s)) else "no")
