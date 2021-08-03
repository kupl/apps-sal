S = input()


def ans147(S: str):
    def_count = 0
    for i in range(int(len(S) / 2)):
        if S[i] != S[-(i + 1)]:
            def_count += 1
    return def_count


print(ans147(S))
