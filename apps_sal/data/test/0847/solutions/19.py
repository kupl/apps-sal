def main():
    pass


def __starting_point():
    main()


(n, x) = list(map(int, input().split()))
numbers = list(map(int, input().split()))
s = abs(sum(numbers))
res = s // x
if s % x != 0:
    res += 1
print(res)
__starting_point()
