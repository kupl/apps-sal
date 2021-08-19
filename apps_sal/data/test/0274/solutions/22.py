def Paint(height, napr):
    return ''


rngOfseq = int(input())
seq = input()
maxh = 3
heightes = []
current = 1
tek = 3
for i in range(rngOfseq - 1):
    if seq[i] == '[' and seq[i + 1] == '[':
        tek += 2
    if seq[i] == ']' and seq[i + 1] == ']':
        tek -= 2
    if maxh < tek:
        maxh = tek
current = maxh
for i in range(rngOfseq - 1):
    heightes.append(current)
    if seq[i] == '[' and seq[i + 1] == '[':
        current -= 2
    if seq[i] == ']' and seq[i + 1] == ']':
        current += 2
heightes.append(current)
current = maxh
Flag = True
for j in range(maxh):
    currentraw = ''
    for i in range(rngOfseq):
        if heightes[i] == current:
            if seq[i] == '[':
                currentraw += '+-'
            else:
                currentraw += '-+'
        elif heightes[i] > current:
            currentraw += '|'
        else:
            currentraw += ' '
        try:
            if heightes[i] == heightes[i + 1]:
                if heightes[i] == current:
                    if seq[i] == '[' and seq[i + 1] == ']':
                        currentraw += ' '
                elif heightes[i] < current:
                    if seq[i] == ']' and seq[i + 1] == '[':
                        currentraw += '  '
                    if seq[i] == '[' and seq[i + 1] == ']':
                        currentraw += ' '
                elif seq[i] == '[' and seq[i + 1] == ']':
                    currentraw += '   '
        except:
            continue
    if current == 1:
        Flag = False
    if Flag:
        current -= 2
    else:
        current += 2
    print(currentraw)
