"""
Created on Thu Oct 10 12:43:24 2013

@author: azimkhan
"""

a = input()
s = []

for c in a.lower():
    if (not c in s):
        s.append(c)

l = len(s)

print("CHAT WITH HER!" if (l % 2 == 0) else "IGNORE HIM!")
