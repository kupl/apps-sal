def ll():
    return list(map(int, input().split()))


testcases = 1
testcases = int(input())
for testcase in range(testcases):
    [n, x] = ll()
    print(2 * x)
