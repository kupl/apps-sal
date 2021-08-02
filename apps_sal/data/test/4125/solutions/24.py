# xi-xが全部Dの倍数になればいい
n, x = list(map(int, input().split()))
pos = list(map(int, input().split()))
diff_pos = [abs(s - x) for s in pos]
min_diff = min(diff_pos)
# print(min_diff)
ans = 0


def main():
    for i in range(min_diff, 0, -1):
        for n in diff_pos:
            if n % i != 0:
                break
            if n == diff_pos[-1]:
                return i


print(main())
