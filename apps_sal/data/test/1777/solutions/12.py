import sys

Ans = 0
N = int(input())
left = {}
right = {}
correct = 0

for i in range(N):
    arr = sys.stdin.readline().strip()
    check = []

    for j in arr:
        if len(check) == 0:
            check.append(j)
        elif j == ")" and check[-1] == "(":
            check.pop()
        else:
            check.append(j)

    leftnum = check.count("(")
    rightnum = check.count(")")
    if leftnum > 0 and rightnum > 0:
        continue
    elif leftnum > 0:
        try:
            left[str(leftnum)] += 1
        except:
            left[str(leftnum)] = 1

    elif rightnum > 0:
        try:
            right[str(rightnum)] += 1
        except:
            right[str(rightnum)] = 1
    else:
        correct += 1


Ans += correct // 2

for key, value in list(left.items()):
    try:
        Ans += min(right[key], value)
    except:
        pass


print(Ans)
