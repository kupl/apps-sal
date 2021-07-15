a = list(map(int, input().split()))
w = min(a[0], a[2], a[3])
am = 256 * w
am += 32 * min(a[0] - w, a[1])
print(am)
