import sys
l = int(sys.stdin.readline())
s = sys.stdin.readline()[:-1]


def check(s):
    n = len(s)
    for i in range(n):
        if s[i] != '9':
            return False
    return True


n = len(s)
if n % l != 0:
    ans = ['0' for _ in range(l)]
    ans[0] = '1'
    x = ['0' for _ in range(l * (n // l + 1))]
    i = 0
    while i < (n // l + 1) * l:
        for j in range(l):
            x[i] = ans[j]
            i += 1
    print(''.join(y for y in x))
else:
    j = l - 1
    # print('divisible')
    carry = 1
    s_ind = ''
    for i in range(l - 1, -1, -1):
        y = (int(s[i]) + carry) % 10
        carry = (int(s[i]) + carry) // 10
        if carry == 0:
            s_ind = str(y)
            break
    # print(i,'ii',carry)
    if carry:
        # print('a')
        if check(s):
            ans = ['0' for _ in range(l)]
            ans[0] = '1'
            i = 0
            # print(ans,'ans')
            x = ['0' for _ in range(l * (n // l + 1))]
            # print(x,'x')
            while i < (n // l + 1) * l:
                for j in range(l):
                    x[i] = ans[j]
                    i += 1
        else:
            x = ['9' for _ in range(l * (n // l + 1))]
        print(''.join(y for y in x))
    else:
        ans = ['0' for _ in range(l)]
        ans[i] = str(y)
        for j in range(i):
            ans[j] = s[j]
        for j in range(i + 1, l):
            ans[j] = '0'
        x = ['0' for _ in range(n)]
        i = 0
        while i < (n // l) * l:
            for j in range(l):
                x[i] = ans[j]
                i += 1
        b = s[:l] * (n // l)
        # print(s[:l])
        # print(b,'s')

        a = ''.join(y for y in x)
        # print(a,'a')
        if a < b:
            print(a)
        else:
            if b > s:
                print(b)
            else:
                print(a)
