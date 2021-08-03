N = int(input())
S = input()


def change():
    s = []
    for i in range(len(S)):
        m = ((ord(S[i]) - ord("A") + N) % 26)
        s.append(chr(m + ord("A")))
    return "".join(s)


print(change())
