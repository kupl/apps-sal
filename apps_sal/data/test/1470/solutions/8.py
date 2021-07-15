def main():
    n = int(input())
    ans = 0
    ans += n // 11 * 2
    if n % 11 <= 6 and n % 11 != 0:
        ans += 1
    elif n % 11 <= 10 and n % 11 > 6:
        ans += 2
    print(ans)
main()

