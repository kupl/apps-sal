def run():
    n = int(input())
    card = input()
    cnt = 0
    start = True
    ans = 0
    last = '.'
    for i in range(n):
        if card[i] == '.':
            cnt += 1
        elif card[i] == 'L':
            if start == True:
                start = False
                cnt = 0
            else:
                ans += cnt % 2
                cnt = 0
            last = 'L'
        else:
            start = False
            ans += cnt
            cnt = 0
            last = 'R'
    if last != 'R':
        ans += cnt
    print(ans)


run()
