N = int(input())


def f(num, use, counter):
    if num > N:
        return
    if use == 0b111:
        counter.append(1)
    f(num * 10 + 7, use | 0b001, counter)
    f(num * 10 + 5, use | 0b010, counter)
    f(num * 10 + 3, use | 0b100, counter)


ans = []
f(0, 0, ans)
print(sum(ans))
