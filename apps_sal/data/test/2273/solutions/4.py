def main():
    from array import array
    from sys import stdin, stdout
    n, m = list(map(int, stdin.readline().split()))
    inp = {tuple(map(int, stdin.readline().split())) for _ in range(m)}
    ans = array('b', (0,)) * (n + 1)
    ans[1] = 1
    c1 = 1
    c2 = c3 = 0
    i = 1
    for j in range(2, n + 1):
        if (1, j) not in inp:
            ans[j] = 1
            c1 += 1
        else:
            if i == 1:
                i = j
            if (i, j) in inp:
                ans[j] = 2
                c2 += 1
            else:
                ans[j] = 3
                c3 += 1
    if m != c1 * (c2 + c3) + c2 * c3 or not c2:
        stdout.write('-1')
    else:
        for i, j in inp:
            if ans[i] == ans[j]:
                stdout.write('-1')
                break
        else:
            stdout.write(' '.join((str(ansi) for ansi in ans if ansi)))


main()
