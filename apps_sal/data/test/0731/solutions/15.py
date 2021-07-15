def number_of_digits(n):
    if n == 0:
        return 0
    else:
        return 1 + number_of_digits(n//10)

def calc(n):
    if n <= 0:
        return 0
    d = number_of_digits(n)
    ret = 0
    for i in range(1,d):
        ret += 9*(10**(i-1))*i
    ret += (n-(10**(d-1))+1)*d

    return ret


def calc2(f,t):
    return calc(t) - calc(f-1)

def solve(w,m,k):
    lower = 0
    upper = m+w
    for i in range(100):
        mid = (lower+upper)//2
        cur = calc2(m,mid)

        if k*cur <= w:
            lower = mid
        else:
            upper = mid

    return lower - m + 1

def main():
    w,m,k = list(map(int,input().split()))
    print(solve(w,m,k))

def __starting_point():
    main()

__starting_point()
