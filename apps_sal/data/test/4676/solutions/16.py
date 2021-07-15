li_o = input()
li_e = input()
an = ''
for i in range(len(li_o)):
    an += li_o[i]
    if i != len(li_e):
        an += li_e[i]
    else:
        break
print(an)
