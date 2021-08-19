t = int(input())
arr = []
for i in range(1, 19):
    arr.append((i - 1) * (i - 2) // 2 * 9 * 9 * 9 + (i - 1) * 9 * 9 + 9)
pref = [0]
for i in arr:
    pref.append(pref[-1] + i)


def f(x):
    if x == 0:
        return 0
    s = str(x)
    n = len(s)
    ans = pref[n - 1]
    cnt = 0
    for i in range(n):
        a = int(s[i])
        if a != 0:
            if cnt == 0:
                ans += (a - 1) * (n - i - 1) * (n - i - 2) // 2 * 9 * 9 + (a - 1) * (n - i - 1) * 9 + (a - 1)
                cnt += 1
            elif cnt == 1:
                ans += (n - i - 1) * (n - i - 2) // 2 * 9 * 9 + (n - i - 1) * 9 + 1
                if a != 1:
                    ans += (a - 1) * (n - i - 1) * 9 + (a - 1)
                cnt += 1
            elif cnt == 2:
                ans += (n - i - 1) * 9 + 1
                if a != 1:
                    ans += a - 1
                cnt += 1
                break
    return ans + 1


for i in range(t):
    (l, r) = map(int, input().split())
    l -= 1
    print(f(r) - f(l))
'n = int(input())\narr1 = list(map(int, input().split()))\nm = int(input())\narr2 = list(map(int, input().split()))\n\nl = 0\nr = 0\nif arr1[l] == arr2[r]\n'
'\nn, k = map(int, input().split())\nprint((k + n - 1) // n)\n'
