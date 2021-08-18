def test():
    from math import factorial as f
    cnt = 0
    i = 1
    for i in range(1, 100 + 1):
        s = str(f(i))
        cnt = 0
        for j in range(len(s) - 1, -1, -1):
            if s[j] == "0":
                cnt += 1
            else:
                break
        print(cnt, end=" ")
        i += 1
    print(cnt, end=" ")


def func(x):
    ans = 0
    while x % 5 == 0:
        x //= 5
        ans += 1
    return ans


def main():
    n = int(input())
    cnt = 0
    i = 1
    while True:
        if i % 5 == 0:
            cnt += func(i)
        if cnt == n:
            print(5)
            print(i, i + 1, i + 2, i + 3, i + 4)
            break
        if cnt > n:
            print(0)
            break
        i += 1


main()
