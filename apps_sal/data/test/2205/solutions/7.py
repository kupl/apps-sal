def main():
    n = int(input())
    nums = list(map(int, input().split()))

    chunk = []
    base = 0
    for i in range(n + 1):
        base ^= i
        chunk.append(base)

    Q = 0
    for i, num in enumerate(nums):
        q = num
        chunks, res = divmod(n, i + 1)
        q ^= chunk[res]
        if chunks % 2 == 1:
            q ^= chunk[i]
        Q ^= q

    print(Q)


main()
