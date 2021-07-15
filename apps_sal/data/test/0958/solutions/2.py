n, k = list(map(int, input().split()))
s = input()
help = []
d = dict()
for i in range(ord('a'), ord('z') + 1):
    if abs(ord('a') - i) > abs(ord('z') - i):
        d[chr(i)] = [abs(ord('a') - i), 'a']
    else:
        d[chr(i)] = [abs(ord('z') - i), 'z']
help = 0
for i in s:
    help += d[i][0]
if help < k:
    print(-1)
else:
    ans = ''
    for i in s:
        if d[i][0] < k:
            ans += d[i][1]
            k -= d[i][0]
        else:
            for j in range(ord('a'), ord('z') + 1):
                if abs(ord(i) - j) == k:
                    ans += chr(j)
                    k -= abs(ord(i) - j)
                    break
    print(ans)


