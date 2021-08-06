n = int(input())
a = list(map(int, input().split()))

inv = False  # even
for i in range(n):
    for j in range(i + 1, n):
        if a[i] > a[j]:
            inv = not inv

m = int(input())

ans = list()
for i in range(m):
    l, r = list(map(int, input().split()))

    if ((r - l + 1) / 2) % 2 == 1 or ((r - l + 1) / 2) % 2 == 1.5:
        inv = not inv

    ans.append(['even', 'odd'][inv])

print('\n'.join(ans))
