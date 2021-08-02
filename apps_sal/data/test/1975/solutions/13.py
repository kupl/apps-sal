def main():
    x, y = map(int, input().split())
    cx = [0] * x
    cy = [0] * y

    print(x + y - 1)
    for i in range(x):
        for j in range(y):
            if cx[i] == 0 or cy[j] == 0:
                print(i + 1, j + 1)
                cx[i] = 1
                cy[j] = 1


main()
