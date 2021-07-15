from collections import Counter

def unbalanced(s):
    c = Counter(s)
    if max(c.values()) > len(s)/2:
        return True
    else:
        return False

s = input()
l = len(s)

balanced = False

for i in range(l-1):
    if unbalanced(s[i:i+2]):
        print(i+1,i+2)
        return

for i in range(l-2):
    if unbalanced(s[i:i+3]):
        print(i+1,i+3)
        return

print(-1,-1)
