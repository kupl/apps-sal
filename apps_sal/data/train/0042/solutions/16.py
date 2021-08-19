import bisect


def solve(s, ans):
    count = 0
    one = []
    n = len(s)
    for i in range(n):
        if s[i] == '1':
            one.append(i)

    for i in range(n):
        curr = 0
        if s[i] == '0':
            start = bisect.bisect(one, i)
            if start < len(one):
                start = one[start]
            else:
                start = n
        else:
            start = i

        # print(i,start)
        for j in range(start, n):
            curr *= 2
            if s[j] == '1':
                curr += 1
            # print(curr,i,j-i+1,j)
            if curr == j - i + 1:
                count += 1

            if curr > n - i:
                break

    ans.append(count)


def main():
    t = int(input())
    ans = []
    for i in range(t):
        s = input()
        solve(s, ans)

    for i in ans:
        print(i)


main()
