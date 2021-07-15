S = input()
T = input()

for i in range(len(S) - len(T)+1):
    target = S[len(S) - len(T) - i:len(S) - i]

    can_search = True
    for key in range(len(T)):
        if target[key] != '?':
            if target[key] != T[key]:
                can_search = False
                break

    if can_search:
        new_key = S[:len(S) - len(T) - i]
        new_key += T
        new_key += S[len(new_key):]
        print((new_key.replace('?', 'a')))
        return

print('UNRESTORABLE')

