n = int(input())
l = list(map(int, list(input())))

def minit(l):
    dec = l[0]
    for i in range(len(l)):
        l[i] = (l[i] - dec + 10) % 10
    return l

ans = [float('+inf')]

for i in range(n):
    mm = minit(l[:])
    ans = min(mm, ans)
    l = l[1:] + [l[0]]

print(''.join(map(str, ans)))

