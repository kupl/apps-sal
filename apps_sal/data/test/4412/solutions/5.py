from collections import defaultdict


def find(A):
    if len(A) == 0:
        return 0
    checked = [0] * len(A)
    temp = []
    for i in range(len(A)):
        if len(temp) < 3 and checked[i] == 0:
            temp += [A[i]]
            for j in range(i + 1, len(A)):
                if A[i] % A[j] == 0:
                    checked[j] = 1
        if len(temp) == 3:
            break

    return sum(temp)


for _ in range(int(input())):
    input()
    dic = defaultdict(int)
    A = list(map(int, input().strip().split(' ')))
    for i in range(len(A)):
        dic[A[i]] = 0
    A = sorted([x for x in dic], reverse=True)
    print(max(find(A), find(A[1:]), find(A[2:]), find(A[3:])))
