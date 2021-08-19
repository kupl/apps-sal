from collections import Counter


def cal(x):
    left = cl = 0
    for i in x:
        if i == "(":
            cl += 1
        if i == ")":
            if cl <= 0:
                left += 1
            else:
                cl -= 1
    return left, cl


n = int(input())
a = [*[x for x in [cal(input()) for i in range(n)] if x[0] == 0 or x[1] == 0]]
left = Counter([i[1] for i in [x for x in a if x[0] == 0]])
right = Counter([i[0] for i in [x for x in a if x[1] == 0]])
ans = 0
#print(left, right)
for i in list(left.keys()):
    ans += (min(left[i], right[i]) if i != 0 else left[i] // 2)
print(ans)
