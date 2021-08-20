s1 = 'qwertyuiop'
s2 = 'asdfghjkl;'
s3 = 'zxcvbnm,./'


def main():
    p = input()
    s = input()
    a = ''
    if p == 'L':
        d = 1
    else:
        d = -1
    for i in s:
        for j in [s1, s2, s3]:
            if i in j:
                q = j.find(i) + d
                q = max(q, 0)
                q = min(len(j) - 1, q)
                a += j[q]
    print(a)


main()
