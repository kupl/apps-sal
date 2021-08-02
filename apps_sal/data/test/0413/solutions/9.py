def fun(n, m):
    if n >= m:
        return (n - m)
    Q = [n]
    mySet = set()
    cnt = 1
    while(True):
        new_Q = []
        for num in Q:
            x = 2 * num
            y = num - 1
            if x == m or y == m:
                return cnt
            if not x in mySet and x < 20000 and x > 0:
                mySet.add(x)
                new_Q.append(x)
            if not y in mySet and y < 20000 and y > 0:
                mySet.add(y)
                new_Q.append(y)
        Q = new_Q
        cnt += 1


n, m = [int(c) for c in input().split()]
print(fun(n, m))
