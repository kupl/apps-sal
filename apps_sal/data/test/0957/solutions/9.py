import sys
import math

s = input()
s2 = "heidi";
ind  = 0;
for i in range(len(s)):
    if s[i] == s2[ind]:
        ind+=1;
    if ind == len(s2):
        break;
if ind == len(s2):
    print("YES")
else:
    print("NO")
