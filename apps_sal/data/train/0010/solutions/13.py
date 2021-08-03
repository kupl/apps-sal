def f(n, l):
    output = [l[0]]
    for i in range(1, n - 1):
        if (l[i] - l[i - 1]) * (l[i + 1] - l[i]) < 0:
            output.append(l[i])
    output.append(l[-1])
    return str(len(output)) + '\n' + ' '.join([str(x) for x in output])


numberofcases = int(input())
for _ in range(numberofcases):
    n = int(input())
    l = [int(t) for t in input().split()]
    print(f(n, l))
