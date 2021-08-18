def main():
    n = int(input())
    s = input()
    if '>' not in s:
        print(n)
    elif '<' not in s:
        print(n)
    else:
        ans = 0
        for i in range(n):
            l = (i - 1 + n) % n
            if s[i] == '-' or s[l] == '-':
                ans += 1
        print(ans)


for _ in range(int(input())):
    main()
