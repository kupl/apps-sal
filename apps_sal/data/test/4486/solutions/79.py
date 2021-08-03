s = str(input())


def answer(s: str) -> str:
    ans = ''
    for i in range(len(s)):
        if i % 2 == 0:
            ans += s[i]
    return ans


print(answer(s))
