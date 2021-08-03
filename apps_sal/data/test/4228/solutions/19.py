N, L = map(int, input().split())
azi = [L + i - 1 for i in range(1, N + 1)]

absmin = L**2

for i in range(N):
    absmin = min(absmin, abs(azi[i]))

if absmin in azi:
    print(sum(azi) - absmin)
else:
    print(sum(azi) + absmin)
