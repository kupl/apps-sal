S = input()


def kaibun():
    count = 0
    for i in range(int(len(S) / 2)):
        if S[i] != S[len(S) - 1 - i]:
            count += 1
    return count


print(kaibun())
