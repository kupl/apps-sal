from collections import *
c=Counter(map(lambda x:x[:-1],open(0)))
for s in["AC","WA","TLE","RE"]:print(s,"x",c[s])
