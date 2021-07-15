def main():
    x, y, z = map(int, input().split())
    a = x // z + y // z
    x %= z
    y %= z
    if x + y < z:
        print(a, 0)
    else:
        print(a + 1, min(z - x, z - y))
    return 0

main()
