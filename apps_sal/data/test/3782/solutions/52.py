def main():
    from collections import Counter as ct
    n, k, q = map(int, input().split())
    a = list(map(int, input().split()))
    c = ct(a).keys()
    a += [0]
    ans = []
    for i in c:
        temp = []
        temp2 = []
        for j in a:
            if j >= i:
                temp2.append(j)
            else:
                if temp2:
                    temp2.sort()
                    if len(temp2) >= k:
                        for l in temp2[:len(temp2)-k+1]:
                            temp.append(l)
                    temp2 = []
        if len(temp) >= q:
            temp.sort()
            ans.append(temp[q-1]-i)
    print(min(ans))


main()
