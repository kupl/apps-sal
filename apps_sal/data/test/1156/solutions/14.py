def check(lst, val):
    return lst[1:] == lst[:-1] and lst[0] == val


n = int(input())
a = [int(s) for s in input().split(' ')]
b_ = [int(s) for s in list(input())]
l = -10 ** 9
r = 10 ** 9
list_ = b_[:4]
for i in range(4, len(b_)):
    if check(list_, 0):
        if b_[i] == 1:
            l = max(max(a[i - 4:i + 1]) + 1, l)
    elif check(list_, 1):
        if b_[i] == 0:
            r = min(r, min(a[i - 4:i + 1]) - 1)
    list_.pop(0)
    list_.insert(len(list_), b_[i])
print(str(l) + ' ' + str(r))
