def main():
    N = int(input())
    txy = [list(map(int, input().split())) for _ in range(N)]
    txy = [[0, 0, 0]] + txy
    # print(txy)
    for i in range(N):
        temp = txy[i + 1][0] - txy[i][0] - abs(txy[i + 1][1] - txy[i][1]) - abs(txy[i + 1][2] - txy[i][2])
        if not (temp % 2 == 0 and temp >= 0):
            print("No")
            return
    print("Yes")


main()
