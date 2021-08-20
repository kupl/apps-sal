(n, h, a, b, k) = list(map(int, input().strip().split()))
for i in range(k):
    (ta, fa, tb, fb) = list(map(int, input().strip().split()))
    if ta == tb:
        print(abs(fa - fb))
    elif fa <= b and fa >= a:
        print(abs(ta - tb) + abs(fa - fb))
    elif fa > b:
        print(fa - b + abs(ta - tb) + abs(b - fb))
    else:
        print(a - fa + abs(ta - tb) + abs(fb - a))
