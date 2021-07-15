def solve(n):
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))[::-1]
    ind = [-1] * (n + 1)
    for i in range(n):
        if i == 0:
            ind[b[i]] = 0
        elif b[i] != b[i - 1]:
            ind[b[i]] = i
    cnt = 0
    for i in range(n):
        if a[i] != b[i]:
            continue
        else:
            swap = 0
            for j in range(b[i] - 1, 0, -1):
                if ind[j] != -1 or ind[j] >= ind[j - 1]:
                    swap = ind[j]
                    ind[j] += 1
                    break
            if n <= swap:
                swap = cnt
                cnt += 1
                cnt %= n
            b[i], b[swap] = b[swap], b[i]
    return a, b


def main():
    n = int(input())
    a, b = solve(n)
    if all(a[i] != b[i] for i in range(n)):
        print("Yes")
        print((" ".join(map(str, b))))
    else:
        print("No")


def __starting_point():
    main()

__starting_point()
