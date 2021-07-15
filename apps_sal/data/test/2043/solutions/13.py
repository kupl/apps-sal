name = input()
phrase = input()
pos = []
j = 0
len_name = len(name)
len_phrase = len(phrase)
test = False
if len_name>=len_phrase:
    print(0)
    return
for n, i in enumerate(phrase):
    if name[j] == i:
        if not test:
            pos.append([n])
            test = True
        j += 1
        if j == len_name:
            pos[-1].append(n)
            test = False
            break

j = 0

for n, i in enumerate(phrase[::-1]):
    if name[len_name-1-j] == i:
        if not test:
            pos.append([len_phrase-n-1])
            test = True
        j += 1
        if j == len_name:
            pos[-1].append(len_phrase-n-1)
            test = False
            break

if pos[0][1] < pos[1][1]:
    print(pos[1][1] - pos[0][1])
else:
    print(0)
