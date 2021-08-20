"""
option 1 : do nothing ( not feasible )
option 2 : take out the head
"""
input()
s = list(input())
removed = False
for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        del s[i]
        removed = True
        break
if not removed:
    del s[-1]
print(''.join(s))
