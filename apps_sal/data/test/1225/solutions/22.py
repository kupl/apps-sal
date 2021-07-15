def mons(hp, attack=1):
    if hp == 1:
        return attack*2-1
    else:
        return mons(hp//2, attack*2)


print((mons(int(input()))))

