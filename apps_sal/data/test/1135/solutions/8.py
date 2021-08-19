n = int(input())
slovo = input()
otvet = ''
while slovo != '':
    en = slovo[0]
    if len(slovo) % 2 == 1:
        otvet = otvet + en
    else:
        otvet = en + otvet
    slovo = slovo[1:]
print(otvet)
