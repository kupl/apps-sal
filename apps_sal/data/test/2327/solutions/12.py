for testcase in range(int(input())):
    n = int(input())
    logs = []
    i = 1
    while i <= n:
        logs.append(i)
        i *= 2
    unfair = 0
    for log in logs:
        unfair += n // log
    print(unfair)
