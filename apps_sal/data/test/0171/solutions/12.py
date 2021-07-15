pw = input()

lg = case = numb = 0

if len(pw) >= 5:
    lg = 1
if pw.lower() != pw and pw.upper() != pw:
    case = 1
for i in pw:
    if i.isnumeric():
        numb = 1

#print(lg, case, numb)

if numb and case and lg:
    print('Correct')
else:
    print('Too weak')

