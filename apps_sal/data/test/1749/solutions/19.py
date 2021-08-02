n, l, r = map(int, input().split())
l -= 1
a = input().split()
b = input().split()

if a[:l] == b[:l] and a[r:] == b[r:]:
    print("TRUTH")
else:
    print("LIE")
