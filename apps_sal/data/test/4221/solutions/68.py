S = list(input())

if (S[-1] == 's'):
    S.append("es")
    print("".join(S))
else:
    S.append("s")
    print("".join(S))
