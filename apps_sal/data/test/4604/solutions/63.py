N = int(input())
(*A,) = sorted(map(int, input().split()))


def f(x):
    for i in range(x, N, 2):
        if A[i - 1] != i or A[i] != i:
            return False
    return True


a = True
if N % 2 == 0:
    a = f(1)
elif A[0] != 0:
    a = False
else:
    a = f(2)
print(2 ** (N // 2) % (10 ** 9 + 7) if a else 0)
