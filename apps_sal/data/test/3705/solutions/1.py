def main():
    n = int(input())
    s = input()
    cnt = 0
    for i in s:
        if i == '8':
            cnt += 1
    print(min(cnt, n // 11))

main()
