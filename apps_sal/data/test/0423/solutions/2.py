n, k = [int(x) for x in input().split()]
L = []
done = 0
for i in range(n + 1):
    c = input()
    if c is '?':
        L.append('?')
    else:
        L.append(int(c))
        done += 1

left = n + 1 - done

if done % 2 == 0:
    chance = 0
else:
    chance = 1

if k == 0:
    if L[0] is '?':
        print('Yes' if chance == 1 else 'No')
    else:
        print('Yes' if L[0] == 0 else 'No')
elif left == 0:
    for i in range(n, 0, -1):
        L[i - 1] += L[i] * k
        if not (-10000000000 < L[i - 1] < 10000000000):
            L[0] = -1
            break
    print('Yes' if L[0] == 0 else 'No')
elif left % 2 == 0:
    if chance == 0:
        print('Yes')
    else:
        print('No')
else:
    if chance == 1:
        print('Yes')
    else:
        print('No')
