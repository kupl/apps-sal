word = list(input())
n = len(word)
emptyword = []
popcount = 0
for i in range(n):
    if len(emptyword) == 0:
        emptyword = [word[i]]
    elif word[i] == emptyword[-1]:
        emptyword.pop()
        popcount += 1
    else:
        emptyword.append(word[i])
if popcount % 2 == 0:
    print('No')
else:
    print('Yes')
