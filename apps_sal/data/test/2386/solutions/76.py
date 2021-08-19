def main():
    N = int(input())
    a_list = list(map(int, input().split()))
    s_list = [n - i for (i, n) in enumerate(a_list)]
    s_list.sort()
    b = s_list[N // 2]
    result = sum((abs(n - b) for n in s_list))
    print(result)


main()
