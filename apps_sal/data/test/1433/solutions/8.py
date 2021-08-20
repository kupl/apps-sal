(n, m) = list(map(int, input().split()))
plan = []
for i in range(n):
    plan.append(input().split())
plan2 = list(map(list, list(zip(*plan))))


def findLeft(string):
    i = 0
    while i < len(string):
        if string[i] == '1':
            return i
        else:
            i += 1


def findRight(string):
    i = len(string) - 1
    while i >= 0:
        if string[i] == '1':
            return i
        else:
            i -= 1


count = 0
for each in plan:
    if each.count('1') == 1:
        count += each.count('0')
    elif each.count('1') > 1:
        l = findLeft(each)
        r = findRight(each)
        count += each[:l].count('0') + 2 * each[l + 1:r].count('0') + each[r + 1:].count('0')
for each in plan2:
    if each.count('1') == 1:
        count += each.count('0')
    elif each.count('1') > 1:
        l = findLeft(each)
        r = findRight(each)
        count += each[:l].count('0') + 2 * each[l + 1:r].count('0') + each[r + 1:].count('0')
print(count)
