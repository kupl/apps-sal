n = int(input())
test = []
test = list(map(int, input().split()))
left = 0
right = len(test) - 1
a = []
b = []
while test:
    if test[left] > test[right]:
        a.append(test[left])
        test.remove(test[left])
        right = len(test) - 1
    else:
        a.append(test[right])
        test.remove(test[right])
        right = len(test) - 1
    if test:
        if test[left] > test[right]:
            b.append(test[left])
            test.remove(test[left])
            right = len(test) - 1
        else:
            b.append(test[right])
            test.remove(test[right])
            right = len(test) - 1
print(sum(a), sum(b))
