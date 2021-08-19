from sys import setrecursionlimit
setrecursionlimit(100000000)


def get_int(string, n):
    i = j = k = 0
    for s in string:
        k += 1
    for s in string:
        if i == n - 1:
            break
        if s == ' ':
            i += 1
        j += 1
    i = 0
    while j < k:
        if string[j] == ' ':
            break
        i = 10 * i + int(string[j])
        j += 1
    return i


d = 'What are you doing at the end of the world? Are you busy? Will you save us?'
a = 'What are you doing while sending "'
b = '"? Are you busy? Will you send "'
c = '"?'
len_a = len(a)
len_b = len(b)
len_c = len(c)
len_d = len(d)
ln = len_a + len_b + len_c
q = int(input())
ls = [len_d]
ans = ''
for i in range(1, 60):
    ls += [ls[i - 1] * 2 + ln]


def get_ans(n, k):
    if n == 0:
        if k > len_d:
            return '.'
        return d[k - 1]
    elif n > 60:
        if k > len_a:
            return get_ans(n - 1, k - len_a)
        else:
            return a[k - 1]
    elif k > ln + 2 * ls[n - 1]:
        return '.'
    elif k > len_a + len_b + 2 * ls[n - 1]:
        return c[k - (len_a + len_b + 2 * ls[n - 1]) - 1]
    elif k > len_a + len_b + ls[n - 1]:
        return get_ans(n - 1, k - len_a - len_b - ls[n - 1])
    elif k > len_a + ls[n - 1]:
        return b[k - len_a - ls[n - 1] - 1]
    elif k > len_a:
        return get_ans(n - 1, k - len_a)
    else:
        return a[k - 1]


for i in range(0, q):
    x = input()
    n = get_int(x, 1)
    k = get_int(x, 2)
    if n > 8698 and k > 295726:
        k -= (n - 1000) * len_a
        ans += get_ans(1000, k)
    else:
        ans += get_ans(n, k)
print(ans)
