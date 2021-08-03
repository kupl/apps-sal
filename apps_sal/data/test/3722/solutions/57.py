import sys
sys.setrecursionlimit(2 * 10**5 + 1)
def input(): return sys.stdin.readline().strip()


n = int(input())
a = input()
b = input()
c = input()
d = input()
mod = 10**9 + 7
e = 1
f = 1
for i in range(n - 3):
    g = (e + f) % mod
    e = f
    f = g
if n <= 3:
    print((1))
else:
    if b == 'B':
        if d == 'B':
            print((1))
        else:
            if c == 'A':
                print((pow(2, n - 3, mod)))
            else:
                print(f)
    else:
        if a == 'A':
            print((1))
        else:
            if c == 'B':
                print((pow(2, n - 3, mod)))
            else:
                print(f)
