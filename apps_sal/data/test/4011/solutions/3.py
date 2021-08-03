def main():
    input()
    n = [int(x) for x in input()]
    f = [0] + [int(x) for x in input().split()]
    for i in range(len(n)):
        if f[n[i]] > n[i]:
            n[i] = f[n[i]]
            for j in range(i + 1, len(n)):
                if f[n[j]] < n[j]:
                    break
                n[j] = f[n[j]]
            break
    print(''.join(str(x) for x in n))


main()
