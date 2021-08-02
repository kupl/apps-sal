import sys
needle = input().strip().lower()
n = int(input())
current = []

for i in range(n):
    temp = input().strip().lower()
    current.append(temp)


def similar(s1, s2):
    if(len(s1) != len(s2)): return False

    l = set(['1', 'l', 'L', 'i', 'I'])
    o = set(['o', 'O', '0'])

    for i in range(len(s1)):
        if(s1[i] == s2[i]): continue
        if(s1[i] in l and s2[i] in l): continue
        if(s1[i] in o and s2[i] in o): continue
        return False

    return True


for item in current:
    if(similar(needle, item)):
        print("No")
        return

print("Yes")
