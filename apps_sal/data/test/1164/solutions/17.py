def fr(s):
    ans = 0
    was = False
    s = s.split('.')
    if len(s[-1]) == 2 and len(s) != 1:
        ans += int(s[-1]) / 100
        was = True

    s = s[::-1]
    for i in range(was, len(s)):
        ans += int(s[i]) * (10 ** (3 * (i - was)))

    return ans


def to(n):
    ans = []
    was = False
    if int(n) != n:
        tmp = str(n - int(n))
        tmp = tmp[2:]
        try:
            if tmp[2]:
                if tmp[2] >= "5":
                    tmp = tmp[0] + str(int(tmp[1]) + 1)
                else:
                    tmp = tmp[:2]
        except:
            pass
        if len(tmp) == 1:
            tmp += '0'
        ans.append(tmp)
        was = True
    n = int(n)

    while n > 0:
        tmp = str(n % 1000)
        if len(tmp) < 3 and n >= 1000:
            tmp = '0' * (3 - len(tmp)) + tmp
        ans.append(tmp)

        n //= 1000
    ans = ans[::-1]
    if was and len(ans) == 1:
        ans = ["0"] + ans

    return ".".join(ans)


s = input() + "a"

data = []
last = 0
number = False
for i in range(len(s)):
    if "a" <= s[i] and s[i] <= "z":
        if number:
            number = False
            data.append(s[last:i])
        continue
    if not number:
        last = i
        number = True

nums = [fr(i) for i in data]

print(to(sum(nums)))
