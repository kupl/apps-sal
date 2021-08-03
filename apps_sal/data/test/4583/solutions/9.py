def kumiawase(S, op, i=0, x=0):
    if i == 4:
        if x == 7:
            print(op + '=7')
            return True
        else:
            return False

    if kumiawase(S, op + '+' + S[i], i + 1, x + int(S[i])):
        return True

    if kumiawase(S, op + '-' + S[i], i + 1, x - int(S[i])):
        return True


S = input()

kumiawase(S, S[0], 1, int(S[0]))
