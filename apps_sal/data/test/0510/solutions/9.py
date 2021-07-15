def main():
    a, b, c, d = map(int, input().split())
    abc = sorted([a, b, c])
    ans = 0
    if abc[1] - abc[0] < d:
        ans += abc[0] + d - abc[1]
    if abc[2] - abc[1] < d:
        ans += abc[1] + d - abc[2]
    print(ans)
    return 0

main()
