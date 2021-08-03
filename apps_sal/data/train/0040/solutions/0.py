def main():
    from sys import stdin, stdout
    for _ in range(int(stdin.readline())):
        n = int(stdin.readline())
        inp1 = [-1] * (n + 1)
        inp2 = [-1] * (n + 1)
        for i, ai in enumerate(map(int, stdin.readline().split())):
            if inp1[ai] < 0:
                inp1[ai] = i
            inp2[ai] = i
        inp1 = tuple((inp1i for inp1i in inp1 if inp1i >= 0))
        inp2 = tuple((inp2i for inp2i in inp2 if inp2i >= 0))
        n = len(inp1)
        ans = 0
        cur = 0
        for i in range(n):
            if i and inp1[i] < inp2[i - 1]:
                cur = 1
            else:
                cur += 1
                ans = max(ans, cur)
        stdout.write(f'{n - ans}\n')


main()
