n = int(input())
a = list(map(int, input().split()))
a_min = min(a)
a_max = max(a)
if a_max - a_min < 2:
    print('{}\n'.format(n), ' '.join(map(str, a)), sep='')
    quit()
a = sorted(list(map(lambda x: x - a_min, a)))
t = [0 for i in range(3)]
for i in a:
    t[i] += 1
c1 = t[1] - t[1] % 2

c2 = min(t[0], t[2]) * 2

print('{}'.format(n - max(c1, c2)))
if c1 > c2:
    print('{} '.format(a_min) * (t[0] + t[1] // 2), '{} '.format(a_max) * (t[2] + t[1] // 2), '{} '.format(a_min + 1) * (t[1] % 2), sep='')
else:
    print('{} '.format(a_min) * (t[0] - c2 // 2), '{} '.format(a_max) * (t[2] - c2 // 2), '{} '.format(a_min + 1) * (t[1] + c2), sep='')
