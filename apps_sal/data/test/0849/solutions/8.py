# B
def main():
    a, b, c, d = list(map(int, input().split()))
    PA = a / b
    PB = c / d
    qA = 1 - PA
    qB = 1 - PB
    print(PA / (1 - qA * qB))


main()
