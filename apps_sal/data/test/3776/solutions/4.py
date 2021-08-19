n = int(input())
(h, m) = input().split(':')
ans = 1000
ans1 = ''
if n == 12:
    (h1, m1) = ('', '')
    for i in range(1, 13):
        for j in range(0, 60):
            h1 = (2 - len(str(i))) * '0' + str(i)
            m1 = (2 - len(str(j))) * '0' + str(j)
            cnt = 4
            if h1[0] == h[0]:
                cnt -= 1
            if h1[1] == h[1]:
                cnt -= 1
            if m1[0] == m[0]:
                cnt -= 1
            if m1[1] == m[1]:
                cnt -= 1
            if cnt < ans:
                ans = cnt
                ans1 = h1 + ':' + m1
    print(ans1)
else:
    (h1, m1) = ('', '')
    for i in range(24):
        for j in range(0, 60):
            h1 = (2 - len(str(i))) * '0' + str(i)
            m1 = (2 - len(str(j))) * '0' + str(j)
            cnt = 4
            if h1[0] == h[0]:
                cnt -= 1
            if h1[1] == h[1]:
                cnt -= 1
            if m1[0] == m[0]:
                cnt -= 1
            if m1[1] == m[1]:
                cnt -= 1
            if cnt < ans:
                ans = cnt
                ans1 = h1 + ':' + m1
    print(ans1)
