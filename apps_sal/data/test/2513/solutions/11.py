from itertools import product

N = int(input())
S = input()
for s1, s2 in product('SW', repeat=2):
    temp = s1 + s2
    for s in S[1:N - 1]:
        if (s == 'o' and temp[-1] == 'S') or (s == 'x' and temp[-1] == 'W'):
            temp += temp[-2]
        else:
            temp += ''.join(set('SW') - set(temp[-2]))
    for i in [N - 1, 0]:
        if S[i] == 'o' and temp[i] == 'S' and temp[(i - 1) % N] == temp[(i + 1) % N]:
            continue
        elif S[i] == 'o' and temp[i] == 'W' and temp[(i - 1) % N] != temp[(i + 1) % N]:
            continue
        elif S[i] == 'x' and temp[i] == 'S' and temp[(i - 1) % N] != temp[(i + 1) % N]:
            continue
        elif S[i] == 'x' and temp[i] == 'W' and temp[(i - 1) % N] == temp[(i + 1) % N]:
            continue
        else:
            break
    else:
        print(temp)
        break
else:
    print(-1)
