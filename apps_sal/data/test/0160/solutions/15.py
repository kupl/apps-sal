from math import sqrt
def Divisor_Set(n):
    s = set()
    for i in range(1, int(sqrt(n))+2):
        if n%i == 0:
            s.add(i)
            s.add(n//i)
    return s

def main():
    n, k = map(int, input().split())
    a = list(map(int, input().split()))
    a_sum = sum(a)
    s = Divisor_Set(a_sum)
    ans = 1
    for v in s:
        a_mod = [x%v for x in a]
        a_mod.sort()
        for i in range(1, n):
            a_mod[i] += a_mod[i-1]
        for i in range(n):
            l, r = a_mod[i], v*(n-i-1) - (a_mod[-1] - a_mod[i])
            if l == r and r <= k:
                if ans < v:
                    ans = v
    print(ans)

def __starting_point():
    main()
__starting_point()
