n = int(input())
letters = set([])
pos = []
s = input()
counter = 0
for c in s:
    if not c in letters:
        letters.add(c)
        pos.append(counter)
        if len(letters)==n:
            break
    counter+=1
if len(letters) != n:
    print("NO")
    return
else:
    print("YES")
    pos.append(len(s))
    for i in range(len(pos)-1):
        print(s[pos[i]:pos[i+1]])
