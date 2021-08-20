S = input()
N = len(S)


def isPalindrome(s):
    n = len(s)
    flag = True
    slist = list(s)
    for (i, c) in enumerate(slist):
        if c != slist[n - 1 - i]:
            flag = False
        if i > n - i:
            break
    return flag


Slist = list(S)
if isPalindrome(S) and isPalindrome(Slist[0:int((N - 1) / 2)]) and isPalindrome(Slist[int((N + 3) / 2) - 1:N]):
    print('Yes')
else:
    print('No')
