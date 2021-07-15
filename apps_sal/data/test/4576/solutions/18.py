def main():
    a, b, c, x = (int(input())+1 for _ in range(4))
    x -= 1

    ans = 0
    for i_a in range(a):
        for i_b in range(b):
            for i_c in range(c):
                if i_a * 500 + i_b * 100 + i_c * 50 == x:
                    ans += 1
    print(ans)


main()
