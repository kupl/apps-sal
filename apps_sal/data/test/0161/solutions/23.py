"""
Created on Sun Mar  3 23:50:56 2019

@author: loyuli
"""
n = int(input())
a = str(bin(n))[2:]
num = a[-1]
an = 0
now = '1'
anp = []
for (idx, i) in enumerate(a):
    if i != now:
        an += 1
        anp.append(len(a) - idx)
        now = i
print(an * 2 - 1 + int(num))
if anp:
    print(' '.join(map(str, anp)))
