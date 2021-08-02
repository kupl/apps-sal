t = int(input())
while t > 0:
    t -= 1
    L, v, l, r = list(map(int, input().split()))
    n = L // v - (r // v) + ((l - 1) // v)
    print(n)
