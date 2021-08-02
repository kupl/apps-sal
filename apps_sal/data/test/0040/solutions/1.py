def sol():
    n = int(input())
    flag = False
    last = None
    for i in range(n):
        a, b = map(int, input().split(' '))
        if a != b:
            return "rated"
        if last is not None and a > last:
            flag = True
        last = a
    if flag:
        return "unrated"
    else:
        return "maybe"


print(sol())
