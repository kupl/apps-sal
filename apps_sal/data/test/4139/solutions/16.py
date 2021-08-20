n = int(input())


def is_753(a):
    check = {'7': 0, '5': 0, '3': 0}
    string = str(a)
    for i in range(len(str(a))):
        if not string[i] in ['7', '5', '3']:
            return False
        check[string[i]] += 1
    for v in check.values():
        if v == 0:
            return False
    return True


q = [3, 7, 5]
count = 0
while len(q) > 0:
    front = q.pop(0)
    if len(str(front)) >= 3 and is_753(front):
        count += 1
    for i in [3, 5, 7]:
        cand = int(str(i) + str(front))
        if cand <= n:
            q.append(cand)
print(count)
