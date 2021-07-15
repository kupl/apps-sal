def r1(t):
    return t(input())

def r2(t):
    return [t(i) for i in input().split()]

for _ in range(int(input())):
    n = r1(int)
    print(n//2)

