sequence=input()
changes=0
even=True
last = sequence[0]
for i in range(0,len(sequence)):
    if last == sequence[i]:
        even = not even
    else:
        if even:
            changes+=1
        even=False
    last = sequence[i]
if even:
    changes+=1
print(changes)
