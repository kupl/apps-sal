from itertools import permutations
import sys
read = sys.stdin.read


def main():
    n = int(input())
    p = "".join(input().split())
    q = "".join(input().split())

    chars = [str(i) for i in range(1, n + 1)]
    per = list(permutations(chars, n))
    per_str = ["".join(pere) for pere in per]
    per_str.sort()
    p_pos = per_str.index(p)
    q_pos = per_str.index(q)
    ans = abs(p_pos - q_pos)
    print(ans)


def __starting_point():
    main()


__starting_point()
