def iroha():
    letter = input()
    vols = ["a", "i", "u", "e", "o"]

    for elm in vols:
        if elm == letter:
            print("vowel")
            return
    
    print("consonant")
            


def __starting_point():
    iroha()


__starting_point()
