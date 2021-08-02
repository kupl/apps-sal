t = int(input())
for t in range(t):
    L, v, l, r = map(int, input().split())
    otv = L // v - r // v + l // v
    if l % v == 0:
        print(otv - 1)
    else:
        print(otv)
