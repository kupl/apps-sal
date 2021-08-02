ll = lambda: list(map(int, input().split()))
testcases = 1
testcases = int(input())
for testcase in range(testcases):
    [a, b, c] = ll()
    print((a + b + c) // 2)
