def main():
    answer = ''
    for query in range(int(input())):
        ans = None
        (x, y) = list(map(int, input().split(' ')))
        if x == 1:
            if y in {1}:
                ans = 'YES'
            else:
                ans = 'NO'
        elif x == 2 or x == 3:
            if y in {1, 2, 3}:
                ans = 'YES'
            else:
                ans = 'NO'
        else:
            ans = 'YES'
        answer += str(ans) + '\n'
    print(answer)


main()
