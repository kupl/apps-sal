from collections import Counter


def get_index(first, ch, i, n):
    for j in range(i, n):
        if first[j] == ch:
            return j
    return -1


n = int(input())
first = input()
second = input()
temp1 = Counter(first)
temp2 = Counter(second)
if temp1 != temp2:
    print(-1)
else:
    first = list(first)
    second = list(second)
    (ans, finalAns) = (0, [])
    for i in range(n):
        if first[i] == second[i]:
            continue
        ind = get_index(first, second[i], i, n)
        ans += ind - i
        for j in range(ind, i, -1):
            finalAns.append(j)
        temp = first.pop(ind)
        first.insert(i, temp)
    print(ans)
    print(*finalAns)
