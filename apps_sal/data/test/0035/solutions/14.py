def check(n, m, fl, count):
    nonlocal flag, tr_flag
    if count == 3:
        return 'NO'
    num = n // 3
    is_ok = set()
    for k in range(0, n, num):
        new_check = set()
        for i in range(k, k + num):
            new_check = new_check | set(fl[i])
        if len(new_check) != 1:
            flag, tr_flag = tr_flag, flag
            if m % 3 == 0:
                return check(m, n, flag, count + 1)
            else:
                return 'NO'
        now = list(new_check)[0]
        if now in is_ok:
            flag, tr_flag = tr_flag, flag
            if m % 3 == 0:
                return check(m, n, flag, count + 1)
            else:
                return 'NO'
        is_ok.add(now)
    return 'YES'


def main():
    nonlocal n, m, flag, tr_flag
    if n % 3 != 0 and m % 3 != 0:
        return 'NO'

    if n % 3 == 0:
        return check(n, m, flag, 0)
    else:
        return check(m, n, tr_flag, 0)


n, m = map(int, input().split())
flag = []
for i in range(n):
    string = list(input())
    flag.append(string)
tr_flag = list(map(list, zip(*flag)))
answer = main()
print(answer)
