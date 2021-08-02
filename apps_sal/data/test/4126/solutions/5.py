s = input()
n = len(s)


def judge_palindrome(s):
    if s == s[::-1]:
        return True
    else:
        return False


if judge_palindrome(s) and judge_palindrome(s[:(n - 1) // 2]) and judge_palindrome(s[(n + 3) // 2 - 1:]):
    ans = 'Yes'
else:
    ans = 'No'
print(ans)
