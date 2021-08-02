N = int(input())

siritolist = []

for i in range(N):
    W = input()
    siritolist.append(W)

for i in range(1, len(siritolist)):
    back_word = list(siritolist[i - 1])
    word = list(siritolist[i])
    if back_word[-1] == word[0] and i > 1:
        for j in range(i - 1):
            if siritolist[i] == siritolist[j]:
                print('No')
                return
    elif back_word[-1] != word[0]:
        print('No')
        return

print('Yes')
