# C - いっしょ
def main():
    import math
    _ = int(input())
    a = list(map(int, input().split()))
    t = float('inf')

    for i in range(min(a), max(a) + 1):
        cnt = 0
        for j in a:
            cnt += (j - i)**2
        else:
            if cnt < t:
                t = cnt
    else:
        print(t)


if __name__ == "__main__":
    main()
