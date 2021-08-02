def main():
    import sys
    input = sys.stdin.readline

    n, *abc = map(int, input().split())
    query = []
    for _ in [0] * n:
        s = input()
        query.append((ord(s[0]) - ord('A'), ord(s[1]) - ord('A')))
    query.append((0, 1))  # 番兵

    ans = ['A'] * n
    for i in range(n):
        a, b = query[i]
        if abc[a] == 0 and abc[b] == 0:
            print("No")
            return
        elif abc[a] == 0:
            abc[a] += 1
            abc[b] -= 1
            ans[i] = chr(ord('A') + a)
        elif abc[b] == 0:
            abc[a] -= 1
            abc[b] += 1
            ans[i] = chr(ord('A') + b)
        else:
            if a in query[i + 1]:
                abc[a] += 1
                abc[b] -= 1
                ans[i] = chr(ord('A') + a)
            else:
                abc[a] -= 1
                abc[b] += 1
                ans[i] = chr(ord('A') + b)
    print("Yes")
    print(*ans, sep=('\n'))


main()
