n = input()
dan = n.count('Danil')
ol = n.count("Olya")
slav = n.count("Slava")
an = n.count("Ann")
nik = n.count("Nikita")
if dan + ol + slav + an + nik == 1:
    print("YES")
else:
    print("NO")
