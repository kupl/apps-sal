import pprint
(n, x, m) = list(map(int, input().split(' ')))


def f(x: int, m: int) -> int:
    return x % m


def solve1(n: int, x: int, m: int) -> int:
    d = {x: 0}
    A = [x]
    ans = A[0]
    loop_count = 0
    for i in range(n):
        A_next = f(A[i] ** 2, m)
        if A_next in d:
            loop_count = (n - d[A_next] - 1) // (d[A[i]] - d[A_next] + 1)
            mod_left = d[A_next]
            mod_right = mod_left + ((n - d[A_next] - 1) % (d[A[i]] - d[A_next] + 1) + 1)
            ans += sum(A[d[A_next]:A[i]]) * (loop_count - 1)
            ans += sum(A[mod_left:mod_right])
            break
        else:
            A.append(A_next)
            d[A_next] = i + 1
            ans += A[i + 1]
    else:
        ans -= A[-1]
    return ans


print(solve1(n, x, m))
