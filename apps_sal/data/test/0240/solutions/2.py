import sys

def main():
    a = sys.stdin.readline().strip()
    b = sys.stdin.readline().strip()

    if a == "01" or a == "10":
        print("0")
        return

    cnt = [0] * 256
    for i in map(ord, a):
        cnt[i] += 1
    n = sum(cnt)

    l = 0
    for i in range(1, 8):
        if i == len(str(n - i)):
            l = n - i
            break;

    for s in b, str(l):
        for i in map(ord, s):
            cnt[i] -= 1

    res = ["".join([b] + [chr(k) * v for k, v in enumerate(cnt) if v > 0 ])] if b[0] > "0" else []

    for i in range(ord("1"), ord("9") + 1):
        if cnt[i] > 0:
            cnt[i] -= 1
            others = [chr(k) * v for k, v in enumerate(cnt) if v > 0]
            others.append(b)
            res.append("".join([chr(i)] + sorted(others)))
            break

    print(min(res))

def __starting_point():
    main()
__starting_point()
