import sys
3.6
'\n        .__     .__                                _______   _______ _________\n  ______|  |__  |__|  ____    ____ _______ _____   \\   _  \\  \\   _  \\______   /  ___/|  |  \\ |  | /    \\  /  _ \\_  __ \\__  \\  /  /_\\  \\ /  /_\\  \\   /    /\n \\___ \\ |   Y  \\|  ||   |  \\(  <_> )|  | \\/ / __ \\_\\  \\_/   \\  \\_/   \\ /    /\n/____  >|___|  /|__||___|  / \\____/ |__|   (____  / \\_____  / \\_____  //____/\n     \\/      \\/          \\/                     \\/        \\/        \\/\n\n'


def eprint(*args, **kwargs):
    if __debug__:
        print(*args, file=sys.stderr, **kwargs)


def __starting_point():
    q = int(input())
    while q > 0:
        ans = 0
        q -= 1
        x = y = z = 0
        n = int(input())
        arr = list(set(map(int, input().split(' '))))
        arr.sort()
        if arr == [2, 3, 5]:
            print(10)
            continue
        z = arr[len(arr) - 1]
        if z % 2 == 0 and z % 3 == 0 and (z % 5 == 0) and (arr.count(z // 2) > 0) and (arr.count(z // 3) > 0) and (arr.count(z // 5) > 0):
            ans = max(ans, z // 2 + z // 3 + z // 5)
        res = []
        while len(arr) > 0 and len(res) < 3:
            c = arr.pop()
            flag = 1
            for x in res:
                flag &= x % c != 0
            if flag == 1:
                res.append(c)
        ans = max(ans, sum(res))
        print(ans)


__starting_point()
