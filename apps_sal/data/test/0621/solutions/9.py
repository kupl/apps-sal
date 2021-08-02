n = input()
s = input().split(" ")
rugi, jumlah, berkas = 0, 0, []
for j, i in enumerate(s):
    if int(i) < 0:
        rugi += 1
        if rugi == 3:
            rugi = 1
            berkas.append(str(jumlah))
            jumlah = 1
        else:
            jumlah += 1
    else:
        jumlah += 1
    if j == len(s) - 1:
        berkas.append(str(jumlah))
print(len(berkas), " ".join(berkas), sep='\n')
