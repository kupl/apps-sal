S = input()
N = len(S)


def is_palindrome(s):
    return s == ''.join(list(reversed(s)))


ans = 'Yes' if is_palindrome(S) and is_palindrome(S[:(N - 1) // 2]) and is_palindrome(S[(N + 1) // 2:]) else 'No'
print(ans)
