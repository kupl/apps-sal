S = input()

def duplicate(seq):
    seen = []
    unique = [x for x in seq if x not in seen and not seen.append(x)]
    return len(seq) != len(unique)

if duplicate(S):
    print('no')
else:
    print('yes')
