S = input()

for i in range(1, len(S)):
    gumozi = S[0:len(S) - i]

    if gumozi[0:len(gumozi) // 2] == gumozi[(len(gumozi) // 2):len(gumozi)]:
        print((len(gumozi)))
        return
print((0))
