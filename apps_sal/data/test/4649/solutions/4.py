def main():
    q = int(input())
    for i in range(q):
        (n, k) = map(int, input().split())
        s = input()
        min_ans = 10 ** 9
        for i in range(n - k + 1):
            count1 = 0
            count2 = 0
            count3 = 0
            for j in range(k):
                if (i + j) % 3 == 0:
                    if s[i + j] != 'R':
                        count1 += 1
                    if s[i + j] != 'G':
                        count2 += 1
                    if s[i + j] != 'B':
                        count3 += 1
                if (i + j) % 3 == 1:
                    if s[i + j] != 'G':
                        count1 += 1
                    if s[i + j] != 'B':
                        count2 += 1
                    if s[i + j] != 'R':
                        count3 += 1
                if (i + j) % 3 == 2:
                    if s[i + j] != 'B':
                        count1 += 1
                    if s[i + j] != 'R':
                        count2 += 1
                    if s[i + j] != 'G':
                        count3 += 1
            min_ans = min(min_ans, count1, count2, count3)
        print(min_ans)


main()
