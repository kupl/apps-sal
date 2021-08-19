def main(n, a):
    if n % 2 == 0:
        a.sort()
        (num0, num1) = (0, 0)
        for (i, x) in enumerate(a):
            if i % 2:
                num0 += x
            else:
                num1 += x
        return num0 != num1
    else:
        return False
        pass


t = int(input())
nary = []
aary = []
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    nary.append(n)
    aary.append(a)
for (n, a) in zip(nary, aary):
    print('First' if main(n, a) else 'Second')
