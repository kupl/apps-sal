def main():
    n = int(input())
    s = input().rstrip()
    ar = [0] * n
    for i in range(n):
        for l in range(1, n):
            j = i
            sum1 = 0
            while j >= 0:
                if s[j] == '*':
                    sum1 += 1
                else:
                    break
                j -= l
            if sum1 >= 5:
                print('yes')
                return
    print('no')
main()


