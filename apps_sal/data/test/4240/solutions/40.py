s = str(input())
t = str(input())

def answer(s: str, t: str) -> str:
    for i in range(len(s)):
        tmp = s[i:] + s[:i]
        if tmp == t:
            return 'Yes'
            break
    else:
        return 'No'

print((answer(s, t)))

