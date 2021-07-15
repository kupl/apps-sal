def main():
    squares = set(str(x * x) for x in range(100000))
    s = input()
    n = len(s)
    ans = float('inf')
    for mask in range(1, (1 << n)):
        o = ''.join([s[i] for i in range(n) if mask & (1 << i) > 0])
        if o[0] == '0':
            continue
        if o in squares:
            pc = bin(mask).count('1')
            ans = min(ans, n - pc)

    if ans == float('inf'):
        ans = -1
    print(ans)

main()

