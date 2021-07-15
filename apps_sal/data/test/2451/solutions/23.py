n, h, a, b, k = list(map(int, input().split()))
for i in range(k):
    ta, fa, tb, fb = list(map(int, input().split()))
    if ta == tb:
        print(abs( fa - fb))
    elif a <= fa <= b:
        print(abs(ta - tb) + abs(fa - fb))
    elif fa > b:
        print(abs(fa - b) + abs(ta - tb) + abs(b - fb))
    elif fa < a:
        print(abs(fa - a) + abs(ta - tb) + abs(a - fb))


