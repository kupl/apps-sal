word = input()
n = len(word)


def vowel(x):
    if x in ['A', 'E', 'I', 'O', 'U', 'Y']:
        return 1
    else:
        return 0


sums = [0] * n
sums[n - 1] = 1 / n
for k in range(n - 2, -1, -1):
    sums[k] = sums[k + 1] + 1 / (k + 1)


def numb(k):
    if k <= (n + 1) // 2:
        return (k + 1) * (sums[k + 1] - sums[n - k - 1]) + (n + 1) * sums[n - k - 1]
    else:
        return numb(n - k - 1)


res = 0
if n == 1:
    res = vowel(word[0])
elif n == 2:
    res = (vowel(word[0]) + vowel(word[1])) * 3 / 2
elif n == 3:
    res = (vowel(word[0]) + vowel(word[2])) * (1 + 1 / 2 + 1 / 3) + 7 / 3 * vowel(word[1])
else:
    for k in range(n):
        res += vowel(word[k]) * numb(k)
print('%.7f' % res)
