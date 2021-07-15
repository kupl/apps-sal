sp = lambda: list(map(int, input().split()))
si = lambda: int(input())

TESTCASES = int(input())
for tc in range(TESTCASES):
    r,g,b=sorted(sp())
    if b>r+g: b=r+g
    print((r+g+b)//2)
