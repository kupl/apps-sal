import sys
import collections

input = sys.stdin.readline


def main():
    t = int(input())
    for _ in range(t):
        S = input().strip()
        M = int(input())
        B = [int(x) for x in input().split()]

        c = collections.Counter(S)
        ans = [""] * M
        ans_rank = [-1] * M
        current = 0

        while sum(B) != -M:
            zero = []
            for i in range(M):
                if B[i] == 0:
                    zero.append(i + 1)
                    B[i] = -1
                    ans_rank[i] = current

            current += 1
            for i in range(M):
                if B[i] == -1:
                    continue
                for z in zero:
                    B[i] -= abs(i + 1 - z)


        for i in range(M):
            if ans_rank[i] == -1:
                ans_rank[i] = current

        c_rank = collections.Counter(ans_rank)

        ma = max(ans_rank)
        c_s = 26
        for i in range(ma + 1):
            ccr = c_rank[i]
            while c[chr(ord('a') + c_s)] < ccr:
                c_s -= 1

            for j in range(M):
                if ans_rank[j] == i:
                    ans[j] = chr(ord('a') + c_s)
            c_s -= 1

        print("".join(ans))


def __starting_point():
    main()

__starting_point()
