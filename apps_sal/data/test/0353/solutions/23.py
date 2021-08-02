def main():
    n = int(input())
    days = list(map(int, input().split()))
    if n == 1:
        if days[0] == 15:
            print("DOWN")
        elif days[0] == 0:
            print("UP")
        else:
            print(-1)
        return
    moves = [1, -1]
    now = 0
    last = days[0]
    if days[1] < days[0]:
        now = (now + 1) % 2
    for i in range(1, n):
        last += moves[now]
        if last == 0 or last == 15:
            now = (now + 1) % 2
    if now == 1:
        print("DOWN")
    else:
        print("UP")


main()
