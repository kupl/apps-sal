n = int(input())
T = input()

mod = None

for i in range(n):
    if T[i] == '0':
        mod = i % 3
        break

if mod is None:
    if n == 1:
        print((2 * 10**10))
    elif n == 2:
        print((10**10))
    else:
        print((0))
    return

for i in range(n):
    if (T[i] == '0') != (i % 3 == mod):
        print((0))
        return

print((10**10 - (n - mod + 4) // 3 + 1))
