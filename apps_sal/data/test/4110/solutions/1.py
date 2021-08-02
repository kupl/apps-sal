def main():
    ans = 1000
    d, g = map(int, input().split())
    pc = [list(map(int, input().split())) for i in range(d)]
    pc.reverse()
    # print(pc)
    for i in range(2 ** d):
        score = 0
        count = 0
        for j in range(d):
            if i & (1 << j):
                score += pc[j][0] * (d - j) * 100 + pc[j][1]
                count += pc[j][0]
        if score >= g:
            if ans > count:
                ans = count
            # print(bin(i),count,score)
            continue
        for j in range(d):
            if not(i & (1 << j)):
                # print("nokori"+str(j))
                c = 0
                for k in range(1, pc[j][0]):
                    score += (d - j) * 100
                    count += 1
                    c += 1
                    if score >= g:
                        if ans > count:
                            ans = count
                        # print(bin(i),j,c,count,score)
                        break
                break
    print(ans)


def __starting_point():
    ans = 0
    main()


__starting_point()
