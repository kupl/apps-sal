import sys
input = sys.stdin.readline
q = int(input())
for i in range(q):
    n, k = map(int, input().split())
    s = input()
    R, G, B = 0, 0, 0
    ans = float('inf')
    for j in range(n):
        if j % 3 == 0:
            if s[j] == 'R':
                G += 1
                B += 1
            elif s[j] == 'G':
                R += 1
                B += 1
            else:
                R += 1
                G += 1
        elif j % 3 == 1:
            if s[j] == 'R':
                G += 1
                R += 1
            elif s[j] == 'G':
                G += 1
                B += 1
            else:
                R += 1
                B += 1
        else:
            if s[j] == 'R':
                R += 1
                B += 1
            elif s[j] == 'G':
                R += 1
                G += 1
            else:
                G += 1
                B += 1
        if j >= k - 1:
            ans = min(ans, R, G, B)
            if (j - k + 1) % 3 == 0:
                if s[j - k + 1] == 'R':
                    G -= 1
                    B -= 1
                elif s[j - k + 1] == 'G':
                    R -= 1
                    B -= 1
                else:
                    R -= 1
                    G -= 1
            elif (j - k + 1) % 3 == 1:
                if s[j - k + 1] == 'R':
                    G -= 1
                    R -= 1
                elif s[j - k + 1] == 'G':
                    G -= 1
                    B -= 1
                else:
                    R -= 1
                    B -= 1
            else:
                if s[j - k + 1] == 'R':
                    R -= 1
                    B -= 1
                elif s[j - k + 1] == 'G':
                    R -= 1
                    G -= 1
                else:
                    G -= 1
                    B -= 1

    print(ans)
