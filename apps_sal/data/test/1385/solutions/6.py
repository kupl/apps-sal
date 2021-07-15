cmd = input()
lexems = []

tmp = ""
bracket = False
word = False

for i in range(len(cmd)):
    if cmd[i]==" ":
        if bracket:
            tmp+=cmd[i]
        elif word:
            lexems.append(tmp)
            tmp=""
            word = False
    elif cmd[i]=='"':
        if bracket:
            lexems.append(tmp)
            tmp=""
            word = False
            bracket = False
        else:
            bracket = True
            word = True
    else:
        tmp+=cmd[i]
        word = True
if tmp!="":
    lexems.append(tmp)
    
for i in lexems:
    print("<",i,">",sep="")

