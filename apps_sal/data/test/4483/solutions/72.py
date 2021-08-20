def main():
    (x, a, b) = (int(input()) for _ in range(3))
    t = x - a
    print(t - b * (t // b))


main()
