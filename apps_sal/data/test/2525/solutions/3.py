def main():
    from collections import deque
    s = deque(input())
    q = int(input())

    flag = 0
    query = []

    for _ in range(q):
        temp = input().split()
        if len(temp) == 1:
            flag += 1
        else:
            query.append(temp + [flag%2])

    for q in query:
        if q[-1] == 0:
            if q[1] == "1":
                s.appendleft(q[2])
            else:
                s.append(q[2])
        else:
            if q[1] == "1":
                s.append(q[2])
            else:
                s.appendleft(q[2])

    if flag % 2 == 1:
        print(("".join(list(s)[::-1])))
    else:
        print(("".join(s)))

main()

