args = input()
def interpreter(arg):
    args = arg.split(' ')
    output = list()
    i = 0
    while i < len(args):
        if args[i] == '':
            pass
        elif args[i][0] == '"':
            if len(args[i]) > 1 and args[i][1] == '"':
                output.append('<>')
            elif len(args[i]) > 1 and args[i][-1] == '"':
                output.append('<' + args[i][1:-1] + '>')
            else:
                if len(args[i]) > 1:
                    output.append('<' + args[i][1:])
                else:
                    output.append('<')
                i += 1
                while len(args[i]) == 0 or args[i][-1] != '"':
                    if args[i] == '':
                        output[-1] = output[-1] + ' '
                    else:
                        output[-1] = output[-1] + ' ' + args[i]
                    i += 1
                if len(args[i]) > 1:
                    output[-1] = output[-1] + ' ' + args[i][:-1] + '>'
                else:
                    output[-1] = output[-1] + ' >'
        else:
            output.append('<' + args[i] + '>')
        i += 1
    return output

for i in interpreter(args):
    print(i)

