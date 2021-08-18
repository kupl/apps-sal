n = int(input())


def digitSum(n):
    s = str(n)
    array = list(map(int, s))
    return sum(array)


print("Yes" if n % digitSum(n) == 0 else "No")
