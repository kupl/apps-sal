#!/usr/bin/env python3

n = int(input())
s = [input() for _ in range(n)]
for i, r in enumerate(s):
    if "OO" in r:
        s[i] = r.replace("OO", "++", 1)
        print("YES")
        print("\n".join(s))        
        break
else:
    print("NO")
        

