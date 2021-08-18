
def INT(): return int(input())
def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())
def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


def do():
    n, k = INTM()
    A = LIST()
    suma = [0] * (n + 1)
    for i in range(n):
        suma[i + 1] = suma[i] + A[i]
    ans = 0
    for i in range(0, n + 1):
        low = i - 1
        high = n + 1
        check = suma[i] + k
        for j in range(20):
            mid = (low + high) // 2
            if suma[mid] < check:
                low = mid
            else:
                high = mid
        ans += n - low
    print(ans)


def __starting_point():
    do()


__starting_point()
