import sys
read = sys.stdin.read
def main():
    def factorization(n):
        arr = []
        temp = n
        for i in range(2, int(-(-n ** 0.5 // 1)) + 1):
            if temp % i == 0:
                cnt = 0
                while temp % i == 0:
                    cnt += 1
                    temp //= i
                arr.append([i, cnt])
        if temp != 1:
            arr.append([temp, 1])
        if not arr:
            arr.append([n, 1])
        return arr

    n = int(input())
    if n == 1:
        print(0)
        return
    ps = [1] * 101
    for i1 in range(2, n + 1):
        i1fac = factorization(i1)
        for face in i1fac:
            ps[face[0]] += face[1]
    o3 = 0
    o5 = 0
    o15 = 0
    o25 = 0
    o75 = 0
    for pse in ps:
        o3 += pse >= 3
        o5 += pse >= 5
        o15 += pse >= 15
        o25 += pse >= 25
        o75 += pse >= 75
    r = o75
    r += o25 * (o3 - 1)
    r += o15 * (o5 - 1)
    if o5 >= 2:
        r += (o5 * (o5 - 1) // 2) * (o3 - 2)
    print(r)

def __starting_point():
    main()
__starting_point()
