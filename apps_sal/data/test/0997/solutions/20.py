inp = input()

inp = inp.replace(',', ';')
tokens = inp.split(';')
# print(tokens);

a = []
b = []
for token in tokens:
    if (token.isdigit() and token[0] != '0') or token == '0':
        a.append(token)
    else:
        b.append(token)

if len(a) is 0:
    print('-')
else:
    print("\"" + ','.join(a) + "\"")

if len(b) is 0:
    print('-')
else:
    print("\"" + ','.join(b) + "\"")
