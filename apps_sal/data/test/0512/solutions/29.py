def main():
    n = int(input())
    ab = [list(map(int, input().split())) for _ in [0]*n]
    d_left = dict()
    d_right = dict()
    s_left = set()
    s_right = set()
    s = set()
    for a, b in ab:
        if a == -1 and b == -1:
            continue
        elif a == -1:
            if b in s:
                print("No")
                return 0
            s_right.add(b)
            s.add(b)
        elif b == -1:
            if a in s:
                print("No")
                return 0
            s_left.add(a)
            s.add(a)
        elif a > b:
            print("No")
            return 0
        else:
            if a in s:
                print("No")
                return 0
            if b in s:
                print("No")
                return 0
            d_left[a] = b
            d_right[b] = a
            s.add(a)
            s.add(b)

    def check(x, y):
        size = (y-x)//2
        for i in range(x, x+size):
            if i in d_left:
                if d_left[i] != i+size:
                    return False
            elif i in s_right:
                return False
            elif i in d_right:
                return False
            elif i in s_left:
                if i+size in s_right:
                    return False
        for i in range(x+size, x+2*size):
            if i in d_right:
                if d_right[i] != i-size:
                    return False
            elif i in s_left:
                return False
            elif i in d_left:
                return False
            elif i in s_right:
                if i-size in s_left:
                    return False
        return True
    dp = [False]*(n+1)
    dp[0] = True

    for i in range(1, n+1):
        for j in range(i-1, -1, -1):
            if dp[j]:
                if check(2*j+1, 2*i+1):
                    dp[i] = True
                    break
    print(["No", "Yes"][dp[-1]])


main()
