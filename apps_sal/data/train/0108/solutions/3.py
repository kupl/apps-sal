def f(a):
    for i in range(len(a)):
        if a[i] < i:
            return i - 1
    return len(a) - 1


def solve(a):
    i = f(a)
    j = len(a) - 1 - f(a[::-1])
    return 'Yes' if i >= j else 'No'


n = int(input())
for i in range(n):
    input()
    a = list(map(int, input().strip().split()))
    print(solve(a))
