import sys
def toInt(x): return int(''.join(map(str, x[-1::-1])))


# sys.stdin=open('note.txt')
pre = 0
ans = [0] * 1000
sum = 0
for n in range(int(input())):
    sum = int(input())
    d = sum - pre
    pre = sum
    if d > 0:
        for i, dig in enumerate(ans):
            if d + dig <= 9:
                ans[i] = dig + d
                break
            d -= 9 - dig
            ans[i] = 9
        print(toInt(ans))
    else:  # d is minus
        d = -d + 1
        d2 = 0
        for i, dig in enumerate(ans):
            d2 += dig
            ans[i] = 0
            if ans[i + 1] < 9 and d2 >= d:
                break

        ans[i + 1] += 1
        d2 -= d
        cnt = d2 // 9
        ans[:cnt] = [9] * cnt
        ans[cnt] = d2 % 9

        print(toInt(ans))
