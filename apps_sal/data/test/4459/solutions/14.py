from collections import Counter

def mapt(fn, *args):
    return tuple(map(fn, *args))


def Input():
    return mapt(int, input().split(" "))


def main():
    n = int(input())
    a = Counter(Input())
    ans = 0
    for key, val in a.items():
        x = val - key
        if x < 0:
            ans += val
        elif x > 0:
            ans += x
    print(ans)


main()
