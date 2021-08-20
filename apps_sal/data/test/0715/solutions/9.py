variants = [len(input()[2:]) for i in range(4)]
is_awesome = [1] * 4
for i in range(4):
    for j in range(4):
        if i != j and (not variants[i] * 2 <= variants[j]):
            is_awesome[i] = 0
    if not is_awesome[i]:
        is_awesome[i] = 1
        for j in range(4):
            if i != j and (not variants[i] / 2 >= variants[j]):
                is_awesome[i] = 0
if sum(is_awesome) == 1:
    print(chr(ord('A') + is_awesome.index(1)))
else:
    print('C')
