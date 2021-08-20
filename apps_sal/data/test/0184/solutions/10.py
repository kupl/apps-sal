(l, r, a) = input().split()
(l, r, a) = (int(l), int(r), int(a))
ans = min([l + a, r + a, int((l + r + a) / 2)])
ans *= 2
print(ans)
