from math import ceil
def find_divisor(n):
    if n == 2:
        return []
    root = ceil(n ** 0.5)
    ans = []
    for i in range(2, root + 1):
        if n % i == 0:
            ans.extend([i, n / i])

    return list(set(ans))

def fans(n):
    div = find_divisor(n)
    if len(div) == 0:
        return n
    else:
        m = min(div)
        divs = True
        for x in div:
            divs = divs and (x % m == 0)
            if divs == False:
                break
        
        if divs: 
            return min(div)
        else:
            return 1

def __starting_point():
    n = int(input())
    print(fans(n))



__starting_point()
