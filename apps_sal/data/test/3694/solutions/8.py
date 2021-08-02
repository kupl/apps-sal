def find(A):
    from collections import defaultdict
    A = sorted(A)
    N = len(A)
    dic = defaultdict(int)
    for i in range(N):
        dic[A[i]] += 1

    checked = []
    count = set([])
    for x in A:
        if dic[x] > 2:
            return "cslnb"
        if dic[x] == 2:
            count.add(x)
            y = x - 1
            if y in dic:
                return "cslnb"
    if len(count) > 1:
        return "cslnb"

    if 0 in count:
        return "cslnb"

    temp = 0
    for i in range(N):
        temp += A[i] - i
    if temp % 2 == 1:
        return "sjfnb"
    return "cslnb"


input()
A = list(map(int, input().strip().split(' ')))
print(find(A))
