s = input()

inside = False
lexeme = []
for c in s:
    if c == '"':
        if inside:
            inside = False
            print("%s>" % ''.join(lexeme))
            lexeme = []
        else:
            lexeme = ['<']
            inside = True
    elif c == ' ':
        if inside:
            lexeme.append(c)
        elif len(lexeme):
            print("%s>" % ''.join(lexeme))
            lexeme = []
    else:
        if len(lexeme):
            lexeme.append(c)
        else:
            lexeme = ['<', c]
if len(lexeme):
    print("%s>" % ''.join(lexeme))
