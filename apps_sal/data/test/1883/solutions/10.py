n = int(input())

t = [0] + list(map(int, input().split()))

a = [0] + list(map(int, input().split()))


ans, cnt = [], [0 for i in range(n + 1)]


for i in a:

    cnt[i] += 1


for i in range(1, n + 1):

    if t[i] == 1:

        crt = [i]

        x = a[i]

        while cnt[x] == 1:

            crt.append(x)

            x = a[x]

        if len(crt) > len(ans):

            ans = crt[:]

ans.reverse()

print(len(ans))

print(' '.join(map(str, ans)))
