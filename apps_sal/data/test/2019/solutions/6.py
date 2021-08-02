for _ in range(int(input())):
    tekst = input()
    i_zer, i_jeden = tekst.count("0"), 0
    i_jeden = len(tekst) - i_zer
    mniejsze = min(i_zer, i_jeden)
    if mniejsze % 2 == 0:
        print("NET")
    else:
        print("DA")
