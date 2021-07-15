def main():
    p = [i for i in range(26)]

    def find(v):
        if p[v] != v:
            p[v] = find(p[v])
        return p[v]

    n = int(input())
    s1 = input()
    s2 = input()

    ans = []

    for i in range(n):
        a = find(ord(s1[i]) - ord('a'))
        b = find(ord(s2[i]) - ord('a'))

        if a != b:
            p[a] = b
            ans.append((chr(ord('a') + a), chr(ord('a') + b)))

    print(len(ans))

    for a, b in ans:
        print(a, b)
        

def __starting_point():
    main()

__starting_point()
