pokemons = ["vaporeon", "jolteon", "flareon", "espeon", "umbreon", "leafeon", "glaceon", "sylveon"]
n = int(input())
s = input()
if n == 6:
    print("espeon")
else:
    for pokemon in pokemons:
        oppor = True
        for i in range(len(s)):
            if len(s) == len(pokemon) and s[i] != '.' and s[i] != pokemon[i]:
                oppor = False
        if len(s) == len(pokemon) and oppor:
            print(pokemon)
            break
