def main():
    n = int(input())
    hts = list(map(int, input().split()))
    ans = []
    max_ht = 0
    m = int(input())
    for i in range(m):
        w, h = list(map(int, input().split()))
        curr_ht = hts[w - 1]
        if max_ht == 0:
            ans.append(curr_ht)
            max_ht = curr_ht + h
        else:
            if curr_ht >= max_ht:
                max_ht = curr_ht + h
                ans.append(curr_ht)
            else:
                ans.append(max_ht)
                max_ht += h

    for i in range(m):
        print(ans[i])


main()
