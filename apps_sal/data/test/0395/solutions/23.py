def main():
    ppl = list(map(int, input().split()))
    strange = sum(ppl)
    if strange % 2 != 0:
        print('NO')
        return
    s1 = strange // 2
    s1 -= ppl[0]
    for i in range(1, 6):
        for k in range(i + 1, 6):
            if ppl[i] + ppl[k] == s1:
                print('YES')
                return
    print('NO')


main()
