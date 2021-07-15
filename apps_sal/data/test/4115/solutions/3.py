import math

s=input()
count=0

for i in range(0,math.floor(len(s)/2)):
    if s[i]!=s[len(s)-i-1]:
        count=count+1

print(count)
