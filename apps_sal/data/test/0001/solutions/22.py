from random import randint

def f(s):
    a = 0
    for i in s:
        a += int(i)
    return a

def solve(n):
    n1 = list(str(n))
    ans = 0
    maxx = 0
    for i in range(len(n1)):
        n2 = n1[:i] + [str(int(n1[i]) - 1)] + ['9' for j in range(len(n1) - i - 1)]
        if f(n2) >= maxx:
            maxx = f(n2)
            ans = n2
    if f(n1) >= maxx:
        maxx = f(n1)
        ans = n1
    return [int(''.join(ans)), maxx]

def tl(n):
    ans = 0
    maxx = 0
    for i in range(1, n + 1):
        if f(list(str(i))) >= maxx:
            maxx = f(list(str(i)))
            ans = i
    return [ans, maxx]

'''for kkk in range(100):
    n = randint(1, 10 ** 5)
    c1 = solve(n)
    c2 = tl(n)
    if c1 != c2:
        print(n)
        print(c1)
        print(c2)
print('ok')'''
n = int(input())
print(solve(n)[0])

