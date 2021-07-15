for eps in range(int(input())):
    n, m = map(int, input().split())
    s = input()
    a = list(map(int, input().split()))
    a.sort()
    ans = [0] * 26
    j = 0
    for i in range(n):
        while j < m and i >= a[j]:
            j += 1
        ans[ord(s[i]) - ord("a")] += m - j + 1
    for elem in ans:
        print(elem, end=" ")
    print()
