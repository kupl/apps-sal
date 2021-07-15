def mons(hp):
    if hp == 1:
        return 1
    else:
        return mons(hp//2)*2 + 1

print((mons(int(input()))))

