s = input()


def answer(s: str) -> int:
    answer = abs(753 - int(s[0] + s[1] + s[2]))
    for i in range(1, len(s) - 2):
        n = s[i] + s[i + 1] + s[i + 2]
        answer = min(answer, abs(int(n) - 753))
    return answer


print(answer(s))
