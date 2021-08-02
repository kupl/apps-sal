def func(N, cur, flg7, flg5, flg3):
    nonlocal count
    if cur > N:
        return

    if flg7 and flg5 and flg3:
        count += 1

    func(N, cur * 10 + 7, 1, flg5, flg3)
    func(N, cur * 10 + 5, flg7, 1, flg3)
    func(N, cur * 10 + 3, flg7, flg5, 1)


N = int(input())
count = 0
func(N, 0, 0, 0, 0)
print(count)
