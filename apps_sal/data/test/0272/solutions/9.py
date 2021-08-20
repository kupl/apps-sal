def main():
    (abra, shacked) = (str(input()), str(input()))
    dictionary = dict()
    for i in range(len(shacked)):
        if not shacked[i] == abra[i]:
            if abra[i] in list(dictionary.values()) and dictionary[abra[i]] != shacked[i]:
                print(-1)
                return
            dictionary[abra[i]] = shacked[i]
            dictionary[shacked[i]] = abra[i]
    making = ''
    for i in range(len(shacked)):
        if shacked[i] in list(dictionary.values()):
            making += dictionary[shacked[i]]
        else:
            making += shacked[i]
    if making != abra:
        print(-1)
        return
    print(int(len(list(dictionary.keys())) / 2))
    for key in list(dictionary.values()):
        if key < dictionary[key]:
            print(key, dictionary[key])


main()
