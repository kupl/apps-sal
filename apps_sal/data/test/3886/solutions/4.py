str0 = 'What are you doing at the end of the world? Are you busy? Will you save us?'
str1 = 'What are you doing while sending "'
str2 = '"? Are you busy? Will you send "'
str3 = '"?'
NMAX = 100010
LMAX = 1e+18 + 69


def solve(n, k):
    while n > 0:
        if k > lg[n]:
            return '.'
        if k <= len(str1):
            return str1[k - 1]
        elif k <= len(str1) + lg[n - 1]:
            k -= len(str1)
        elif k <= len(str1) + lg[n - 1] + len(str2):
            return str2[k - len(str1) - lg[n - 1] - 1]
        elif k <= len(str1) + lg[n - 1] + len(str2) + lg[n - 1]:
            k -= len(str1) + lg[n - 1] + len(str2)
        else:
            return str3[k - len(str1) - lg[n - 1] - len(str2) - lg[n - 1] - 1]
        n -= 1
    if k <= len(str0):
        return str0[k - 1]
    return '.'


lg = [0] * NMAX
lg[0] = len(str0)
for i in range(1, NMAX):
    lg[i] = 2 * lg[i - 1] + len(str1) + len(str2) + len(str3)
    if lg[i] > LMAX:
        lg[i] = LMAX
q = int(input())
while q > 0:
    (n, k) = map(int, input().split())
    print(solve(n, k), end='')
    q -= 1
