for nt in range(int(input())):
    n = int(input())
    if n >= 1 and n <= 9:
        print(1)
        print(n)
        continue
    s = str(n)
    count = 0
    ans = []
    for i in range(len(s)):
        if s[i] != '0':
            count += 1
            ans.append(s[i] + '0' * (len(s) - i - 1))
    print(count)
    print(*ans)
