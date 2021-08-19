import itertools


def main():
    N = int(input())
    cnt = 0
    for i in range(3, len(str(N)) + 1):
        for j in itertools.product([3, 5, 7], repeat=i):
            p = 0
            for (a, b) in enumerate(j[::-1]):
                p += b * 10 ** a
            if p > N:
                break
            if len(set(j)) == 3:
                cnt += 1
    print(cnt)


main()
