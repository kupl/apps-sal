S = input()
odd = ['R', 'U', 'D']
even = ['L', 'U', 'D']
for x in range(len(S)):
    if (x+1) % 2 == 0:
        if not S[x] in even:
            print('No')
            break
    else:
        if not S[x] in odd:
            print('No')
            break
else:
    print('Yes')
