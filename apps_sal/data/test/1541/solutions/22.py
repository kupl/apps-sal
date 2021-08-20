s = input().split('^')
s[0] = s[0][::-1]


def m(k):
    return sum(((ord(s[k][i]) - ord('0')) * (i + 1) for i in range(len(s[k])) if s[k][i] != '='))


(a, b) = (m(0), m(1))
print('left' if a > b else 'right' if a < b else 'balance')
