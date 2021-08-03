def main():
    S = input()
    K = int(input())
    cnt = 0
    n = 0
    for i in S:
        if i == '1':
            cnt += 1
        else:
            n = int(i)
            break
    if cnt >= K:
        print(1)
    else:
        print(n)
    return


main()
