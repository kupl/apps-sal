def cmp(o1, o2):
    result = 0
    for i in range(6):
        if o1[i] != o2[i]:
            result += 1
    return result


count = int(input())
lst = []
for i in range(count):
    lst += [str(input())]
if count == 1:
    print(6)
    return

div = 6
for n in range(1, count):
    for i in range(n - 1, -1, -1):
        div = min(div, cmp(lst[n], lst[i]))
        if div <= 2:
            print(0)
            return
if div >= 5:
    print(2)
elif div >= 3:
    print(1)
