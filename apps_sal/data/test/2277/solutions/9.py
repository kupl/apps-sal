n = int(input())

s = list(map(int, input().split()))

t = False   #even

for i in range(n):
    for j in range(i + 1, n):
        if s[i] > s[j]:
            t = not t

m = int(input())

a = []

for h in range(m):
    l, r = map(int, input().split())
    if ((r - l + 1) / 2) % 2 == 1 or ((r - l + 1) / 2) % 2 == 1.5:
        t = not t

    a.append(['even', 'odd'][t])

print('\n'.join(a))
