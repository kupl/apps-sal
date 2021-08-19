w = sorted(input())
total = False
if len(w) == 1:
    total = True
    print('No')
else:
    for i in range(0, len(w), 2):
        if w[i] != w[i + 1]:
            print('No')
            total = True
            break
if total == False:
    print('Yes')
