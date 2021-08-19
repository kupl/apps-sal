N = int(input())


def f(num, use, counter):
    if num > N:
        return
    if use == 7:
        counter.append(1)
    f(num * 10 + 7, use | 1, counter)
    f(num * 10 + 5, use | 2, counter)
    f(num * 10 + 3, use | 4, counter)


ans = []
f(0, 0, ans)
print(sum(ans))
