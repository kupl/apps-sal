# import sys
# sys.stdin = open("F:\\Scripts\\input","r")
# sys.stdout = open("F:\\Scripts\\output","w")

MOD = 10**9 + 7
I = lambda: list(map(int, input().split()))

n, = I()
if (n - 2) % 3 == 0:
    print(1, 2, n - 3)
    return
print(1, 1, n - 2)
