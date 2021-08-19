def is_kaibun(string):
    for i in range(len(string) // 2 + 1):
        if string[i] != string[len(string) - i - 1]:
            return False
    else:
        return True


S = input()
if is_kaibun(S) and is_kaibun(S[0:(len(S) - 1) // 2]) and is_kaibun(S[(len(S) + 3) // 2 - 1:len(S)]):
    print('Yes')
else:
    print('No')
